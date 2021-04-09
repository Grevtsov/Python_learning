def my_func(x, y):
    """
    Функция возведения числа в отрицательную степень
    :param x: float
    :param y: int

    :result: my_func(5, -2):
    0.04000
    """

    y = abs(y)
    while x == 0:
        x = float(input('Введите число, которое хотите возвести в степень: '))
    res = 1
    while y > 0:
        res = res * x
        y = y - 1
    return 1 / res


x = float(input('Введите число, которое хотите возвести в степень: '))
y = int(input('Введите степень. Целое отрицательное число : '))
print(f'{my_func(x, y):.5f}')
