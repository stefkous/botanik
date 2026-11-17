from types import MappingProxyType

from botanik.tile import Tile, AllTiles, SourceTile
from botanik.config import PlayerID
from dataclasses import dataclass
import typing
from typing import Mapping


@dataclass(frozen=True)
class TilePosition:
    x: int
    y: int

SOURCE_POSITION = TilePosition(x=0, y=0)

@dataclass(frozen=True)
class Machine:
    tiles: Mapping[TilePosition, Tile | SourceTile]

    def __post_init__(self):
        if not isinstance(self.tiles.get(SOURCE_POSITION), SourceTile):
            raise ValueError(f"Machine must have a SourceTile at position {SOURCE_POSITION}, got {self.tiles.get(SOURCE_POSITION)}")
        # initialise machine
        object.__setattr__(self, 'tiles', MappingProxyType(self.tiles))

    @classmethod
    def new(cls, player_id: PlayerID)-> "Machine":
        if player_id not in typing.get_args(PlayerID):
            raise ValueError(f"player_id must be one of {typing.get_args(PlayerID)}, got {player_id}")
        return cls(tiles = {SOURCE_POSITION: SourceTile(belongs_to_player=player_id)}
            )

    @property
    def source(self) -> SourceTile:
        return self.tiles[SOURCE_POSITION]

    @property
    def player_id(self) -> PlayerID:
        return self.source.belongs_to_player

    def with_tile(self, position: TilePosition, tile: Tile) -> "Machine":
        if position in self.tiles:
            raise ValueError(f"position {position} already occupied by {self.tiles[position]}")
        return Machine(tiles={**self.tiles, position: tile})