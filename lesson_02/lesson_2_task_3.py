import math


def square(side):

    area = side * side
    # Округляем вверх (math.ceil вернет целое число)
    return math.ceil(area)


# Пример 1: Целое число (5 * 5 = 25)
print(f"Сторона 5 -> Площадь: {square(5)}")

# Пример 2: Дробное число (3.1 * 3.1 = 9.61 -> округление вверх до 10)
print(f"Сторона 3.1 -> Площадь: {square(3.1)}")
