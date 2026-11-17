from enum import IntEnum, StrEnum
from typing import Literal, NamedTuple
import typing

PlayerID = Literal[1,2]
ColumnIDs = Literal["A", "B", "C", "D", "E"]
Flowers = Literal[0,1,3]

class TileTypes(StrEnum):
    plant = "plant"
    vegetable = "vegetable"
    meca_botanist = "meca_botanist"
    cross = "cross"
    tee = "tee"
    straight = "straight"
    corner = "corner"

class Colours(StrEnum):
    green = "green"
    blue = "blue"
    red = "red"
    yellow = "yellow"
    black = "black"

class Side(IntEnum):
    top = 0
    right = 1
    bottom = 2
    left = 3

class TypeFeatures(NamedTuple):
    sides: frozenset[Side]
    flowers: list[Flowers]

type_mapping: dict[TileTypes, TypeFeatures] = {
    TileTypes.plant: TypeFeatures(frozenset({2}), [3]),
    TileTypes.vegetable: TypeFeatures(frozenset({2}), [3]),
    TileTypes.meca_botanist: TypeFeatures(frozenset(), [0]),
    TileTypes.cross: TypeFeatures(frozenset({0,1,2,3}), [0]),
    TileTypes.tee: TypeFeatures(frozenset({1,2,3}), [0,0,1]),
    TileTypes.straight: TypeFeatures(frozenset({0,2}), [0,0,1]),
    TileTypes.corner: TypeFeatures(frozenset({1,2}), [0,0,1])
}

TOTAL_TILES = sum(len(type_mapping[tile_type].flowers) for tile_type in TileTypes) * len(Colours)