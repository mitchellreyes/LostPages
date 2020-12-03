import enum
import random


class Color(enum.Enum):
    red = 1
    black = 2
    blue = 3
    colorless = 4


class Potion:
    def __init__(self, c=None):
        if not c:
            c = random.choice(list(Color))
        self.color = c

    def change_color(self, c):
        self.color = c
