import pytest
from botanik.board import Board, Column
from botanik.config import Colours, TileTypes
from botanik.tile import Tile

TILE = Tile(id=1, 
            color=Colours.green, 
            type=TileTypes.plant, 
            flowers=3)


def make_column(column_id: str) -> Column:
    """Build a minimal valid column with the given id."""
    return Column(id=column_id, central_tiles=[TILE], players_tiles={1: TILE, 2: None})


def test_column() -> None:
    column = make_column("A")
    assert column.id == "A"
    assert column.central_tiles == [TILE]
    assert column.players_tiles == {1: TILE, 2: None}


def test_column_rejects_empty_central_tiles() -> None:
    with pytest.raises(ValueError, match="central_tiles must have at least 1 tile, got 0"):
        Column(id="A", central_tiles=[], players_tiles={1: TILE, 2: None})


@pytest.mark.parametrize(
    "players_tiles",
    [
        pytest.param({1: TILE}, id="missing-player"),
        pytest.param({1: TILE, 3: None}, id="wrong-player-id"),
    ],
)

def test_column_rejects_invalid_players(players_tiles: dict) -> None:
    with pytest.raises(ValueError, match="players_tiles must have entries for both players"):
        Column(id="A", central_tiles=[TILE], players_tiles=players_tiles)


def test_board() -> None:
    board = Board(columns=[make_column(column_id) for column_id in "ABCDE"])
    assert [column.id for column in board.columns] == list("ABCDE")


def test_board_rejects_wrong_column_count() -> None:
    with pytest.raises(ValueError, match="board must have 5 columns, got 1"):
        Board(columns=[make_column("A")])


def test_board_rejects_duplicate_column_ids() -> None:
    with pytest.raises(ValueError, match="board column ids must be"):
        Board(columns=[make_column("A") for _ in range(5)])
