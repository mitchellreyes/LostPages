import enum
import random
import math
from potion import Potion, Color


class SpellType(enum.Enum):
    Attack = 1
    Modifier = 2
    Defense = 3
    Spell = 4


class Page:
    # st = spell type
    # t = title
    # desc = description
    # val = an option to set value of page on creation
    # pot = an option to set cost of a page on creation
    # pot_amt = amount of potions to make this page cost

    def __init__(self, st=None, base=False, t="", desc="", val=None, pot=None, pot_amt=1):
        self.value = 0
        self.cost = {}
        self.title = t
        self.description = desc
        if not st:
            st = random.choice(list(SpellType))
        self.__spell_type = st
        if base:
            v = 1 if not val else val
            self.set_value(v)
            self.add_cost_value(pot, amt=pot_amt) if pot else self.roll_cost_value()
        else:
            self.roll_value()
        self.page = eval(self.__spell_type.name)()

    def get_spell_type(self):
        return self.__spell_type

    def get_value(self):
        return self.value

    def get_cost(self):
        return self.cost

    def roll_value(self, mod=0):
        v = int(round(random.random(), 2) * 100) + mod
        if math.isclose(round(random.random(), 4), 0.9999, abs_tol=0.0001):
            self.set_value(10)
            self.roll_cost_value()
        elif 99 >= v > 97:
            self.set_value(random.randint(7, 9))
            self.roll_cost_value(amt=random.randint(4, 6))
        elif 97 >= v > 87:
            self.set_value(random.randint(3, 6))
            self.roll_cost_value(amt=random.randint(2, 4))
        else:
            self.set_value(1)
            self.roll_cost_value()

    def set_value(self, v):
        self.value = v

    def add_cost_value(self, pot: Potion, amt=1):
        for i in range(amt):
            if pot.color.name not in self.cost:
                self.cost.update({pot.color.name: [pot]})
            else:
                self.cost[pot.color.name].append(pot)

    def roll_cost_value(self, amt=1):
        self.cost.clear()
        for i in range(amt):
            p = Potion()
            if p.color.name not in self.cost:
                self.cost.update({p.color.name: [p]})
            else:
                self.cost[p.color.name].append(p)
            p = None

    def roll_value_w_mod(self, m):
        self.roll_value(mod=m)

    def print_cost(self):
        for key in self.get_cost():
            print(("\t\t{}x {} " + ("potion" if len(self.cost[key]) == 1 else "potions"))
                  .format(len(self.cost[key]), key))


class Attack(Page):
    def __init__(self):
        print('')


class Modifier(Page):
    def __init__(self):
        print("")


class Defense(Page):
    def __init__(self):
        print("")


class Spell(Page):
    def __init__(self):
        print("")