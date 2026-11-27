from dataclasses import dataclass
from botanik.config import TOTAL_TILES, TileTypes, type_mapping, Colours, Flowers, PlayerID, Side

@dataclass(frozen=True)
class Tile:
    id: int
    color: Colours 
    type: TileTypes
    flowers: Flowers

    def __post_init__(self) -> None:
        # check the id is from 0-65 and unique
        if not 0 <= self.id <= 64:
            raise ValueError(f"tile id is out of range, should be between {range(0,64)}")
        if self.type not in list(TileTypes.__members__.values()):
            raise ValueError(f"tile type not recognized: {self.type}")
        if self.color not in list(Colours.__members__.values()):
            raise ValueError(f"tile color not recognized: {self.color}")
        if self.flowers not in list(Flowers.__members__.values()):
            raise ValueError(f"tile flowers not recognized: {self.flowers}")
        object.__setattr__(self, 'id', self.id)
        object.__setattr__(self, 'color', self.color)
        object.__setattr__(self, 'flowers', self.flowers)
        object.__setattr__(self, 'type', self.type)

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
        if len(self.tiles) != len(set((tile.id, tile.color, tile.type, tile.flowers) for tile in self.tiles)):
            raise ValueError(f"AllTiles must contain unique tiles, got {len(self.tiles)} tiles with {len(set((tile.id, tile.color, tile.type, tile.flowers) for tile in self.tiles))} unique tiles")
        # check that all tiles are valid
        for tile in self.tiles:
            if tile.type not in list(TileTypes.__members__.values()):
                raise ValueError(f"tile type not recognized: {tile.type}")
            if tile.color not in list(Colours.__members__.values()):
                raise ValueError(f"tile color not recognized: {tile.color}")
            if tile.flowers not in list(Flowers.__members__.values()):
                raise ValueError(f"tile flowers not recognized: {tile.flowers}")

            
@dataclass(frozen=True)
class SourceTile:
    belongs_to_player: PlayerID
    open_side: Side = Side.bottom
    