from dataclasses import dataclass
import typing
from botanik.config import TOTAL_TILES, TileTypes, type_mapping, Colours, Flowers, PlayerID, Side

@dataclass(frozen=True)
class Tile:
    id: int
    color: Colours 
    type: TileTypes
    flowers: Flowers

    def __post_init__(self) -> None:
        if self.type not in list(TileTypes.__members__.keys()):
            raise ValueError(f"tile type not recognized: {self.type}")

    @property
    def open_sides(self) -> frozenset[Side]:
        return type_mapping[self.type].sides

@dataclass(frozen=True)
class AllTiles:
    tiles: list[Tile]

    def __post_init__(self) -> None:
        # number of tiles must match the total number of tiles in the game
        if len(self.tiles) != TOTAL_TILES:
            raise ValueError(f"AllTiles must contain {TOTAL_TILES} tiles, got {len(self.tiles)}")
        # check more specifics - unique
        if len(self.tiles) != len(set((tile.color, tile.type, tile.flowers) for tile in self.tiles)):
            raise ValueError(f"AllTiles must contain unique tiles, got {len(self.tiles)} tiles with {len(set((tile.color, tile.type, tile.flowers) for tile in self.tiles))} unique tiles")

@dataclass(frozen=True)
class SourceTile:
    belongs_to_player: PlayerID
    open_side: Side = Side.bottom
    