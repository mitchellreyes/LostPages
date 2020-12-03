from page import Page, SpellType
from player import Player
from potion import Potion, Color


def main():
    player1 = Player()
    base = [Page(st=SpellType.Attack, t="Big Sword", desc="+2 to melee", val=2, base=True,
                 pot=Potion(Color.red), pot_amt=2),
            Page(st=SpellType.Attack, t="Small Dagger", desc="+1 to melee", base=True,
                 pot=Potion(Color.colorless)),
            Page(st=SpellType.Defense, t="Wood Shield", desc="+1 to defense", base=True,
                 pot=Potion(Color.red)),
            Page(st=SpellType.Spell, t="Chicken Wing", desc="+1 to hp", base=True,
                 pot=Potion(Color.black)),
            Page(st=SpellType.Modifier, t="Hot Sauce", desc="+1 to spells", base=True,
                 pot=Potion(Color.blue))]
    player1.add_potion(Potion(c=Color.colorless), val=2)
    player1.add_potion(Potion(c=Color.red))
    for p in base:
        player1.add_page(p)

    player1.print_potion_pool()

    for pg in player1.get_book():
        print("({}) {}:\n\t[{}]".format(pg.get_spell_type().name, pg.title, pg.description))
        pg.print_cost()
        print('\n')


if __name__ == "__main__":
    main()
