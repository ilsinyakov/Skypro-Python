def month_to_season(number):
    if number in (12, 1, 2):
        return 'Зима'
    elif number in range(3, 6):
        return 'Весна'
    elif number in range(6, 9):
        return 'Лето'
    elif number in range(9, 12):
        return 'Осень'
    else:
        return 'Вы ввели несуществующий номер месяца'

print(month_to_season(11))
