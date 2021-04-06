# seasons = {
#     12: 'Зима',
#     1: 'Зима',
#     2: 'Зима',
#     3: 'Весна',
#     4: 'Весна',
#     5: 'Весна',
#     6: 'Лето',
#     7: 'Лето',
#     8: 'Лето',
#     9: 'Осень',
#     10: 'Осень',
#     11: 'Осень',
# } Первый вариант решения
month = input('Введите порядковый номер месяца: ')
while not month.isdigit() or int(month) < 1 or int(month) > 12:
    month = (input('Введите корректный номер месяца (от 1 до 12): '))
month = int(month)
# print(seasons.get(month))
seasons = {
    'Зима': [1, 2, 12],
    'Весна': [3, 4, 5],
    'Лето': [6, 7, 8],
    'Осень': [9, 10, 11],
}
for key, value in seasons.items():
    if month in value:
        print(key)
