def divide(x, y):
    """
    Функция возвращает деление порвого (x) числа на второе (y)

    (x, y) -> float

    >>> divide(4, 2)
    2
    """

    while y == 0:
        y = float((input('На "0" делить нельзя! Введите знаменатель: ')))
    return x / y


# Решение 2

def divide_2():
    """
    Функция возвращает деление порвого числа на второе.
    Входные данные запрашивает у пользователя, и проверяет данные на валидность

    (x, x) -> float

    >>> divide_2(4, 2)
    2
    """
    x = input('введите числитель: ')
    y = input('введите знаменатель: ')
    while True:
        if x.isdigit():
            break
        else:
            x = input('Введите числитель: ')
    while True:
        if y.isdigit():
            break
        else:
            y = (input('Введите знаменатель: '))
    while True:
        if float(y) == 0:
            y = input('На "0" делить нельзя! Введите знаменатель: ')
        else:
            break
    x = float(x)
    y = float(y)
    return x / y


print(divide(5, 10))
print(divide_2())
