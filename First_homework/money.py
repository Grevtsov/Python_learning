revenue = float(input('Введите значение выручки вышей фирмы: '))
expenses = float(input('Введите значение издержек вышей фирмы: '))
if revenue > expenses:
    profit = revenue / expenses
    print('Рентабельность фирмы составляет {:.2f}'.format(profit))
    number_employees = float(input('Введите количество сотрудников фирмы: '))
    emp_profit = (revenue - expenses) / number_employees
    # print(f'Прибыль в рассчёте на одного сотрудника составит {emp_profit}') #проболвал разные варианты форматирования
    print('Прибыль в рассчёте на одного сотрудника составит %.2f' % emp_profit)
else:
    print('Фирма работает в убыток')
