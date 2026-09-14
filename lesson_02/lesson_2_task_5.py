months = [
    "Январь",
    "Февраль",
    "Март",
    "Апрель",
    "Май",
    "Июнь",
    "Июль",
    "Август",
    "Сентябрь",
    "Октябрь",
    "Ноябрь",
    "Декабрь",
]
season = ["Весна", "Лето", "Зима", "Осень"]


def month_to_season(month):
    if month >= 0 and month <= 2:
        return season[2]
    # elif month >= 3 and month <= 5:
    #     return season[0]  # Возвращает "Весна"
    # elif month >= 6 and month <= 8:
    #     return season[1]  # Возвращает "Лето"
    # elif month >= 9 and month <= 11:
    #     return season[3]  # Возвращает "Осень"
    # else:
    #     return "Неверный номер"


print(season[2])
# print(season[0])
# print(season[1])
# print(season[3])
