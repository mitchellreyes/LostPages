from page import Page
from player import Player


def main():
    player1 = Player()
    for i in range(6):
        p = Page()
        player1.add_page(p)
        p = None

    for pg in player1.get_book():
        print("{} page:\n\tPower {}".format(pg.get_spell_type().name, pg.get_value()))
        pg.print_cost()
        print('\n')


if __name__ == "__main__":
    main()
