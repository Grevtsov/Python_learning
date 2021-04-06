seasons = ['Зима', 'Весна', 'Лето', 'Осень']
month = input('Введите порядковый номер месяца: ')
while not month.isdigit() or int(month) < 1 or int(month) > 12:
    month = (input('Введите корректный номер месяца (от 1 до 12): '))
month = int(month)
if 1 <= month <= 2 or month == 12:
    print(seasons[0])
elif 3 <= month <= 5:
    print(seasons[1])
elif 6 <= month <= 8:
    print(seasons[2])
else:
    print(seasons[3])
