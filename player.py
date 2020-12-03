class Player:
    MAX_PAGE_AMOUNT = 5
    book = []
    attack_val = 1
    defense_val = 1
    spell_pow = 1
    health = 10

    def add_page(self, page):
        if len(self.book) + 1 <= self.MAX_PAGE_AMOUNT:
            self.book.append(page)
        else:
            print("You have reached the max amount of pages in your book")
            return

    def get_book(self):
        return self.book
