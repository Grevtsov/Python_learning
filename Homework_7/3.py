from math import ceil


class Cell:

    def __init__(self, num):
        self.num = int(num)

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num - other.num < 0:
            print('Клетка уничтожена!')
        else:
            return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        if self.num // other.num < 1:
            return ceil(self.num / other.num)
        else:
            return self.num // other.num

    def make_order(self, num_raw):
        result = []
        for i in range(int(self.num / num_raw)):
            result.append('*' * num_raw)
        result.append('*' * (self.num % num_raw))
        return '\n'.join(result)


cell_1 = Cell(5)
cell_2 = Cell(10)
cell_3 = Cell(113)
print(cell_1 + cell_3)
print(cell_2 + cell_1)
print(cell_2 - cell_3)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_3 / cell_1)
print(cell_3.make_order(20))
