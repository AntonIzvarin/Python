nums = [
    1,
    2,
    "Fizz",
    4,
    "Buzz",
    "Fizz",
    7,
    8,
    "Fizz",
    "Buzz",
    11,
    "Fizz",
    13,
    14,
    "FizzBuzz",
    16,
    17,
]


def fizz_buzz(n):

    for nums in range(1, n + 1):
        # 1. Проверяем текущее число (nums) на деление на 3 и 5
        if nums % 3 == 0 and nums % 5 == 0:
            print("FizzBuzz")
        # 2. Проверяем текущее число на деление на 3
        elif nums % 3 == 0:
            print("Fizz")
        # 3. Проверяем текущее число на деление на 5
        elif nums % 5 == 0:
            print("Buzz")
        # 4. Теперь else внутри цикла! Если ни одно условие выше не подошло:
        else:
            print(nums)


fizz_buzz(17)
