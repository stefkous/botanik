from dataclasses import dataclass
import typing
from botanik.config import ColumnIDs, PlayerID
from botanik.tile import Tile

@dataclass(frozen=True)
class Column:
    id: ColumnIDs 
    central_tiles: tuple[Tile, ...] #last one is the top tile
    players_tiles: tuple[Tile | None, Tile | None] # index 0 is player 1, index 1 is player 2

    def __post_init__(self):
        # check how many player registries we have & which ones
        if len(self.players_tiles) != 2:
            raise ValueError(f"players_tiles must be exactly 2, got {len(self.players_tiles)}")
        object.__setattr__(self, 'central_tiles', tuple(self.central_tiles))
        object.__setattr__(self, 'players_tiles', tuple((self.players_tiles)))


    @classmethod
    def new(cls, id: ColumnIDs) -> "Column":
        return cls(
            id=id,
            central_tiles=(),
            players_tiles=(None, None)
        ) 

    
    @property
    def top_central_tile(self) -> Tile | None:
        return self.central_tiles[-1] if self.central_tiles else None


    def get_player_tile(self, player_id: PlayerID) -> Tile | None:
        return self.players_tiles[player_id - 1]

    
    def update_central_tile(self, new_central_tile: Tile) -> "Column":
        return Column(
            id=self.id,
            central_tiles=self.central_tiles + (new_central_tile,),
            players_tiles=self.players_tiles
        )


    def update_player_tile(self, player_id: PlayerID, new_player_tile: Tile|None) -> "Column":
        return Column(
            id=self.id,
            central_tiles=self.central_tiles,
            players_tiles=self.players_tiles[:player_id - 1] + (new_player_tile,) + self.players_tiles[player_id:]
        )


    def swap_central_tile_with_meca_botanist(self, incoming_tile: Tile | None) -> "Column":
        if incoming_tile is None:
            # check that the column has at least one central tile to swap with 
            if len(self.central_tiles) == 0:
                raise ValueError(f"cannot swap same central tile with meca botanist, no central tiles in column {self.id}")
            return Column(
                id=self.id,
                central_tiles=self.central_tiles[:-1],
                players_tiles=self.players_tiles
            )
        else:
            return self.update_central_tile(incoming_tile)



@dataclass(frozen=True)
class Board:
    columns: tuple[Column, ...] # must be 5 columns

    def __post_init__(self):
        if len(self.columns) != 5:
            raise ValueError(f"board must have 5 columns, got {len(self.columns)}")
        for col in self.columns:
            if col.id not in typing.get_args(ColumnIDs):
                raise ValueError(f"column ID {col.id} is not defined")

