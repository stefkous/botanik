from botanik.config import TileTypes, Colours
from botanik.tile import Tile
from botanik.board import Column, Board

test_tile = Tile(id=1, color=Colours.green, type=TileTypes.plant, flowers=3)

def test_column():
    column = Column(
        id="A",
        central_tiles=[test_tile],
        players_tiles={1: test_tile, 2: None},
    )
    assert column.id == "A"
    assert column.central_tiles == [test_tile]
    assert column.players_tiles[1] == test_tile
    assert column.players_tiles[2] is None

def test_invalid_column():
    try:
        invalid_column = Column(
            id="A",
            central_tiles=[],
            players_tiles={1: test_tile, 2: None},
        )
    except ValueError as e:
        assert str(e) == "central_tiles must have at least 1 tile, got 0"

def test_board():
    column_a = Column(
        id="A",
        central_tiles=[test_tile],
        players_tiles={1: test_tile, 2: None},
    )
    column_b = Column(
        id="B",
        central_tiles=[test_tile],
        players_tiles={1: None, 2: test_tile},
    )
    column_c = Column(
        id="C",
        central_tiles=[test_tile],
        players_tiles={1: test_tile, 2: test_tile},
    )
    column_d = Column(
        id="D",
        central_tiles=[test_tile],
        players_tiles={1: None, 2: None},
    )
    column_e = Column(
        id="E",
        central_tiles=[test_tile],
        players_tiles={1: test_tile, 2: None},
    )
    board = Board(columns=[column_a, column_b, column_c, column_d, column_e])
    assert len(board.columns) == 5
    assert board.columns[0].id == "A"
    assert board.columns[1].id == "B"
    assert board.columns[2].id == "C"
    assert board.columns[3].id == "D"
    assert board.columns[4].id == "E"

def test_invalid_board():
    try:
        invalid_board = Board(columns=[Column(
            id="A",
            central_tiles=[test_tile],
            players_tiles={1: test_tile, 2: None},
        )])
    except ValueError as e:
        assert str(e) == "board must have 5 columns, got 1"

def test_invalid_players_tiles():
    try:
        invalid_column = Column(
            id="A",
            central_tiles=[test_tile],
            players_tiles={1: test_tile},
        )
    except ValueError as e:
        assert str(e) == "players_tiles must have entries for both players 1 and 2, got dict_keys([1])"
