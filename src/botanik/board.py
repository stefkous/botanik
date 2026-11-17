from dataclasses import dataclass
import typing
from botanik.config import ColumnIDs, PlayerID
from botanik.tile import Tile

@dataclass(frozen=True)
class Column:
    id: ColumnIDs 
    central_tiles: list[Tile] #last one is the top tile
    players_tiles: dict[PlayerID, Tile|None]

    def __post_init__(self):
        # check how many player registries we have & which ones
        if len(self.players_tiles) != 2:
            raise ValueError(f"players_tiles must have entries for both players 1 and 2, got {self.players_tiles.keys()}")
        if not all(player in self.players_tiles for player in typing.get_args(PlayerID)):
                    raise ValueError(f"players_tiles must have entries for both players 1 and 2, got {self.players_tiles.keys()}")
        
        # check the central registry has at least one tile
        if len(self.central_tiles) < 1:
            raise ValueError(f"central_tiles must have at least 1 tile, got {len(self.central_tiles)}")

@dataclass(frozen=True)
class Board:
    columns: list[Column]

    def __post_init__(self):
        if len(self.columns) != 5:
            raise ValueError(f"board must have 5 columns, got {len(self.columns)}")
        for col in self.columns:
            if col.id not in typing.get_args(ColumnIDs):
                raise ValueError(f"column ID {col.id} is not defined")