class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(' '.join(map(str, el)) for el in self.lists)

    def __add__(self, other):
        errors = []
        if len(self.lists) != len(other.lists):
            errors.append('Количество строк матриц должно быть одинаковым')
        elif [True] == [1 for i in range(len(self.lists)) if len(self.lists[i]) != len(other.lists[i])]:
            errors.append('Количество столбцов матриц должено быть одинаковым')
        try:
            return '\n'.join(' '.join(map(str, el))
                             for el in [[self.lists[i][j] + other.lists[i][j]
                                         for j in range(len(self.lists[0]))] for i in range(len(self.lists))])
        except NameError:
            errors.append('Для ввода данных матрица допустимы только числа')
        except TypeError:
            errors.append('Для ввода данных матрица допустимы только числа')
        except IndexError:
            pass
        if errors:
            for error in errors:
                print(error)


c = Matrix([[1, 2, 3], [1, 5, 3], [0, 2, 1], [1, 2, 3]])
d = Matrix([[2, 2, 2], [2, 2, 2], [1, 3, 5], [0, 0, 1]])

print(c, '\n')
print(d, '\n')
print(c+d)
