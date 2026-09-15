class Card:

    def __init__(self, number, date, holder):
        self.holder = holder
        self.number = number
        self.valid_date = date

    def pay(self, amount):
        print("с карты", self.number, "списали", amount)