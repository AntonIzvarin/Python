rate = input("Оцените работу оператора от 1 до 5:")
rate_as_number = int(rate)

if (rate_as_number < 1):
    rate_as_number = 1

if (rate_as_number > 5):
    rate_as_number = 5

if rate_as_number == 1:
    feedback = input("Расскажите что Вас не устроило: ")
elif rate_as_number == 2:
    feedback = input ("Что вас смутило?: ")
elif rate_as_number == 3:
    feedback = input ("Можно расскачазть более подробнее?: ")
elif rate_as_number == 4:
    feedback = input ("Расскажите что понравилось особенно?: ")
else:
    feedback = input ("Посоветуете ли вы нас другим?: ")

print(feedback)