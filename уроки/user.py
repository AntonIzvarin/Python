class User:

    def __init__(self, name):
        print("я создался")
        self.username = name
        self.age = 0  # Теперь у каждого пользователя свой собственный возраст!

    def say_name(self):  # В Python принято использовать snake_case (say_name вместо sayName)
        print("Меня зовут", self.username)

    def say_age(self):
        print(self.age)

    def set_age(self, new_age):
        self.age = new_age

    def addCard(self, card):
        self.card = card

    def getCard(self):
        return self.card