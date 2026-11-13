from typing import Literal, NamedTuple

PlayerID = Literal[1,2]
Colors = Literal["green", "blue", "red", "yellow", "black"]
Types = Literal["plant", "vegetable", "meca-botanist", "cross", "tee", "straight", "corner"]
Flowers = Literal[0,1,3]
Side = Literal[0,1,2,3]
SourceTiles = Literal["male", "female"]
sides_mapping = {0:"top",
                 1:"right",
                 2:"bottom",
                 3:"left"}

class TypeFeatures(NamedTuple):
    sides: frozenset[Side]
    flowers: list[Flowers]

type_mapping: dict[Types, TypeFeatures] = {
    "plant": TypeFeatures(frozenset({2}), [3]),
    "vegetable": TypeFeatures(frozenset({2}), [3]),
    "meca-botanist": TypeFeatures(frozenset(), [0]),
    "cross": TypeFeatures(frozenset({0,1,2,3}), [0]),
    "tee": TypeFeatures(frozenset({1,2,3}), [0,0,1]),
    "straight": TypeFeatures(frozenset({0,2}), [0,0,1]),
    "corner": TypeFeatures(frozenset({1,2}), [0,0,1])
}