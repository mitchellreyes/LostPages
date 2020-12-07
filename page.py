import enum
import random
import math
from potion import Potion, Color


class SpellType(enum.Enum):
    Attack = 1
    Modifier = 2
    Defense = 3
    Spell = 4


'''
Page
    Title (Name of the page)
    Description (Description of what the page does)
    Value (Value to be modified or modify by)
    Cost (Number of potions it takes to play this page)
    SpellType (Determine what type of Page this is)
    Capabilities [] (Possible SpellType(s) this page could be used on)
'''
class Page:
    def __init___(self, title="", desc="", val=0, cost=[], st=None, cap=[]):
        self.title = title
        self.description = desc
        self.value = val
        self.cost = cost
        self.spell_type = st
        self.capabilities = cap

    def get_cost(self):
        return self.cost

    def add_cost(self, p: Potion):
        self.cost.append(p)

    def remove_cost_by_color(self, col: Color):
        for p in self.cost:
            if p.get_color() == col:
                self.cost.remove(p)
                return

    def remove_cost_by_potion(self, pot: Potion):
        for p in self.cost:
            if p == pot:
                self.cost.remove(p)
                return
