from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from itertools import count


class TileTypes(Enum):
    DOTS = auto()
    STICKS = auto()
    CRACKS = auto()
    DRAGON = auto()
    WIND = auto()

    def __str__(self):
        return f'{self.name}'.capitalize()


class DragonValues(Enum):
    GREEN = auto()
    RED = auto()
    WHITE = auto()

    def __str__(self):
        return f'{self.name}'.capitalize()


class WindValues(Enum):
    NORTH = auto()
    WEST = auto()
    SOUTH = auto()
    EAST = auto()

    def __str__(self):
        return f'{self.name}'.capitalize()


@dataclass(slots=True)
class Tile:
    _id: int
    suit: TileTypes
    value: int | DragonValues | WindValues
    red: bool = False

    def __lt__(self, other: Tile):
        return self._id < other._id

    def __eq__(self, other: Tile):
        return (self.suit, self.value) == (other.suit, other.value)

    def __str__(self):
        if self.suit in (TileTypes.DRAGON, TileTypes.WIND):
            return f'{self.value} {self.suit}'.capitalize()
        return f'{self.value} of {self.suit}'.capitalize()


def initialize_tiles():
    ids = count()
    all_tiles = []
    for tile_type in TileTypes:
        if tile_type == TileTypes.DRAGON:
            for color in DragonValues:
                all_tiles.extend([Tile(next(ids), tile_type, color) for _ in range(4)])
        elif tile_type == TileTypes.WIND:
            for direction in WindValues:
                all_tiles.extend([Tile(next(ids), tile_type, direction) for _ in range(4)])
        else:
            for i in range(1, 10):
                all_tiles.extend([Tile(next(ids), tile_type, i) for _ in range(4)])
    return all_tiles


if __name__ == "__main__":
    print(initialize_tiles())
