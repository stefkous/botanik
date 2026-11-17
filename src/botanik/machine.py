from botanik.tile import Tile, AllTiles, SourceTile
from botanik.board import Column, Board
from dataclasses import dataclass


@dataclass
class Position:
    x: int
    y: int

@dataclass
class Machine:
    player_id: int
    tiles: dict[Tile, position]
