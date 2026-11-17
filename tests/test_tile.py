from dataclasses import replace

import pytest

from botanik.config import Colours, Side, TileTypes, type_mapping
from botanik.tile import AllTiles, SourceTile, Tile


def build_deck() -> list[Tile]:
    """Build the full deck described by config, one id per tile."""
    specs = [
        (colour, tile_type, flowers)
        for colour in Colours
        for tile_type in TileTypes
        for flowers in type_mapping[tile_type].flowers
    ]
    return [
        Tile(id=i, color=colour, type=tile_type, flowers=flowers)
        for i, (colour, tile_type, flowers) in enumerate(specs)
    ]


@pytest.fixture
def plant_tile() -> Tile:
    return Tile(id=1, color=Colours.green, type=TileTypes.plant, flowers=3)


def test_tile_properties(plant_tile: Tile) -> None:
    assert plant_tile.id == 1
    assert plant_tile.color == Colours.green
    assert plant_tile.type == TileTypes.plant
    assert plant_tile.flowers == 3
    assert plant_tile.open_sides == frozenset({Side.bottom})


@pytest.mark.parametrize("tile_type", list(TileTypes))
def test_tile_accepts_every_type(tile_type: TileTypes) -> None:
    flowers = type_mapping[tile_type].flowers[0]
    tile = Tile(id=1, color=Colours.red, type=tile_type, flowers=flowers)
    assert tile.type == tile_type


def test_tile_rejects_unknown_type() -> None:
    with pytest.raises(ValueError, match="tile type not recognized: invalid_type"):
        Tile(id=2, color=Colours.red, type="invalid_type", flowers=1)


def test_tile_rejects_flowers_not_allowed_for_type() -> None:
    with pytest.raises(ValueError, match="plant tile cannot have 0 flowers"):
        Tile(id=1, color=Colours.green, type=TileTypes.plant, flowers=0)


def test_all_tiles_accepts_full_deck() -> None:
    deck = build_deck()
    assert AllTiles(tiles=deck).tiles == deck


def deck_missing_a_tile() -> list[Tile]:
    return build_deck()[:-1]


def deck_with_duplicate_id() -> list[Tile]:
    deck = build_deck()
    return [*deck[:-1], replace(deck[-1], id=deck[0].id)]


def deck_with_wrong_composition() -> list[Tile]:
    deck = build_deck()
    plant = next(tile for tile in deck if tile.type == TileTypes.plant)
    swapped = replace(plant, type=TileTypes.vegetable)
    return [swapped if tile is plant else tile for tile in deck]


@pytest.mark.parametrize(
    ("make_tiles", "message"),
    [
        pytest.param(deck_missing_a_tile, "must contain 65 tiles", id="wrong-count"),
        pytest.param(deck_with_duplicate_id, "unique tile ids", id="duplicate-id"),
        pytest.param(deck_with_wrong_composition, "does not match", id="wrong-composition"),
    ],
)
def test_all_tiles_rejects_invalid_deck(make_tiles, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        AllTiles(tiles=make_tiles())


def test_source_tile_defaults_to_bottom() -> None:
    source_tile = SourceTile(belongs_to_player=1)
    assert source_tile.belongs_to_player == 1
    assert source_tile.open_side == Side.bottom


def test_source_tile_rejects_unknown_player() -> None:
    with pytest.raises(ValueError, match="3 is not a valid PlayerID"):
        SourceTile(belongs_to_player=3)
