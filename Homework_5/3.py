# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, \
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. \
# Выполнить подсчет средней величины дохода сотрудников.


with open(r"staff_members.txt", "r", encoding="utf-8") as f:
    low_paid_staff = []
    salary = []
    for line in f:
        try:
            if float(line.split()[1]) < 20000:
                low_paid_staff.append(line.split()[0])
            salary.append(line.split()[1])
        except IndexError:
            pass
    print('Список сотрудников с зарплатой менее 20000:')
    for i, el in enumerate(low_paid_staff, 1):
        print(f'{i} - {el}')
    print()
    print(f'Средняя зарплата сотрудников - {sum(map(float, salary))/len(salary):.2f} рублей')
