from potion import Potion
from page import Page

class Player:
    MAX_PAGE_AMOUNT = 5

    def __init__(self):
        self.book = []
        self.potions = {}
        self.attack_val = 1
        self.defense_val = 1
        self.spell_pow = 1
        self.health = 10

    def add_page(self, page: Page):
        if len(self.book) + 1 <= self.MAX_PAGE_AMOUNT:
            self.book.append(page)
        else:
            print("You have reached the max amount of pages in your book")
            return

    def get_book(self):
        return self.book

    def add_potion(self, pot: Potion, val=1):
        for i in range(val):
            if pot.color.name not in self.potions:
                self.potions.update({pot.color.name: [pot]})
            else:
                self.potions[pot.color.name].append(pot)

    def print_potion_pool(self):
        print("Potion pool:")
        for key in self.potions:
            print(("\t{}x {} " + ("potion" if len(self.potions[key]) == 1 else "potions"))
                  .format(len(self.potions[key]), key))
        print("\n")


