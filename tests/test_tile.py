from botanik.config import TileTypes, Colours, Side
from botanik.tile import Tile, AllTiles, SourceTile

test_tile = Tile(id=1, color=Colours.green, type=TileTypes.plant, flowers=3)

def test_tile_properties():
    assert test_tile.id == 1
    assert test_tile.color == Colours.green
    assert test_tile.type == TileTypes.plant
    assert test_tile.flowers == 3
    assert test_tile.open_sides == frozenset({2})

def test_invalid_tile_type():
    try:
        invalid_tile = Tile(id=2, color=Colours.red, type="invalid_type", flowers=1)
    except ValueError as e:
        assert str(e) == "tile type not recognized: invalid_type"

def test_all_tiles():
    all_tiles = AllTiles(tiles=[test_tile])
    assert len(all_tiles.tiles) == 1
    assert all_tiles.tiles[0] == test_tile

def test_invalid_all_tiles():
    try:
        invalid_all_tiles = AllTiles(tiles=[test_tile, test_tile])
    except ValueError as e:
        assert str(e) == "AllTiles must contain unique tiles, got 2 tiles with 1 unique tiles"

def test_source_tile():
    source_tile = SourceTile(belongs_to_player=1, open_side=Side.bottom)
    assert source_tile.belongs_to_player == 1
    assert source_tile.open_side == Side.bottom

def test_invalid_source_tile():
    try:
        invalid_source_tile = SourceTile(belongs_to_player=3, open_side=Side.bottom)
    except ValueError as e:
        assert str(e) == "3 is not a valid PlayerID"
