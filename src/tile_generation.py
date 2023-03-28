from dataclasses import dataclass, field
from enum import Flag, auto
from itertools import count


class TileTypes(Flag):
    DRAGON = auto()
    WIND = auto()
    DOTS = auto()
    STICKS = auto()
    CRACKS = auto()
    HONORS = DRAGON | WIND


class DragonValues(Flag):
    GREEN = auto()
    RED = auto()
    WHITE = auto()


class WindValues(Flag):
    NORTH = auto()
    WEST = auto()
    SOUTH = auto()
    EAST = auto()


@dataclass(slots=True)
class Tile:
    suit: TileTypes
    value: int | DragonValues | WindValues
    _id: int = field(default_factory=count().__next__)
    red: bool = False


def initialize_tiles():
    all_tiles = []
    for tile_type in TileTypes:
        if tile_type & TileTypes.DRAGON:
            for color in DragonValues:
                all_tiles.extend([Tile(tile_type, color) for _ in range(4)])
        elif tile_type & TileTypes.WIND:
            for direction in WindValues:
                all_tiles.extend([Tile(tile_type, direction) for _ in range(4)])
        else:
            for i in range(1, 10):
                all_tiles.extend([Tile(tile_type, i) for _ in range(4)])
    return all_tiles


if __name__ == "__main__":
    print(initialize_tiles())
