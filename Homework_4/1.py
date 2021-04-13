from sys import argv

# Скрипт с параметрами

script_name, working_hours, wage, bonus = argv
print(f'Зарплата сотрудника за этот период составит: {(float(working_hours) * float(wage) + float(bonus)):0.2f} рублей')


# Скрипт с вводам данных в командную строку

# script_name = argv
# working_hours = float(input("Выработка в часах : "))
# wage = float(input("Ставка: "))
# bonus = float(input("Премия: "))
# print(f'Зарплата сотрудника за этот период составит: {(working_hours * wage + bonus):0.2f} рублей')
