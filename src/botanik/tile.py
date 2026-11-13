from dataclasses import dataclass
from typing import Literal
from config import type_openings_mapping, Colors, Types, Flowers, SourceTiles, PlayerID

@dataclass(frozen=True)
class Tile:
    id: int
    color: Colors 
    type: Types
    flowers: Flowers

    def __post_init__(self):
        if not 0 <= self.id < 65:
            raise ValueError(f"tile id out of range: {self.id}")

    @property
    def openings(self):
        return len(type_openings_mapping[self.type])

    @property
    def open_sides(self):
        return type_openings_mapping[self.type]

@dataclass(frozen=True)
class SourceTile:
    gender: SourceTiles
    belongs_to_player: PlayerID
    opening: int = 1
    

    