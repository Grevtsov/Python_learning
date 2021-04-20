# Задание 3.
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}

    @property
    def income(self):
        return self._income


class Position(Worker):
    def get_full_name(self):
        return f'Полное имя сотрудника - {self.surname} {self.name}'

    def get_total_income(self):
        return f'Полный доход сотрудника - {sum(self._income.values()):.02f}'


a = Position('Viktor', 'Panda', 'CEO', 3000, 5000)
b = Position('John', 'Wei', 'Cleaner', 10000, 12000)

print(a.name, a.surname, a.position, a.income)
print(b.name, b.surname, b.position, b.income)
print(a.get_full_name())
print(a.get_total_income())
print(b.get_full_name())
print(b.get_total_income())
