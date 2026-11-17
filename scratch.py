from botanik.tile import Tile, AllTiles, SourceTile
from botanik.board import Column, Board
from botanik.config import Colours, TileTypes, Side

tile_one = Tile(id=1, color=Colours.green, type=TileTypes.plant, flowers=3)
a = Column(
    id="A",
    central_tiles=[tile_one],
    players_tiles={1: tile_one, 2: None}
)
b = Column(
    id="B",
    central_tiles=[tile_one],
    players_tiles={1: None, 2: tile_one}
)
c = Column(
    id="C",
    central_tiles=[tile_one],
    players_tiles={1: tile_one, 2: tile_one}
)
d = Column(
    id="D",
    central_tiles=[tile_one],
    players_tiles={1: None, 2: None}
)
e = Column(
    id="E",
    central_tiles=[tile_one],
    players_tiles={1: tile_one, 2: None}
)
board = Board(columns=[a, b, c, d, e])


print("done")