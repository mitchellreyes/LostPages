import enum
import random
import math


class SpellType(enum.Enum):
    Attack = 1
    #Modifier = 2
    #Defense = 3
    #Spell = 4


class Page:
    # Attack = dmg value
    # Modifier = modifier value for dmg/defense value
    # Defense = defense value
    value = 0

    def __init__(self):
        self.__spell_type = random.choice(list(SpellType))
        self.page = eval(self.__spell_type.name)()

    def get_value(self):
        return self.value

    def set_value(self, v):
        self.value = v

    def roll_value(self, mod=0):
        v = int(round(random.random(), 2) * 100) + mod
        if math.isclose(round(random.random(), 2), 0.99, abs_tol=0.01):
            self.set_value(10)
        elif 99 >= v > 95:
            self.set_value(random.randint(7, 9))
        elif 95 > v > 70:
            self.set_value(random.randint(3, 6))
        else:
            self.set_value(random.randint(1, 3))

    def roll_value_w_mod(self, m):
        self.roll_value(mod=m)


class Attack(Page):
    def __init__(self):
        self.roll_value()
        print("Attack page created with power {}!".format(self.get_value()))


class Modifier(Page):
    def __init__(self):
        print("Modifier page created!")


class Defense(Page):
    def __init__(self):
        print("Defense page created!")


class Spell(Page):
    def __init__(self):
        print("Spell page created!")