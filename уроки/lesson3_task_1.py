from user import User
from card import Card

alex = User("Aleks")

alex.say_name()
alex.say_age()
alex.set_age(23)

# Создаём карту в переменную card1
card1 = Card("1234 4321 0000 1234", "11/23", "Alex F")

#Передаём именно объект card1, а не класс Card
alex.addCard(card1)

# Теперь оплата пройдёт успешно!
alex.getCard().pay(1000)
