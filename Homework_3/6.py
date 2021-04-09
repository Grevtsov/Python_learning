def int_func(word):
    return word.capitalize()


def ext_func():
    words = input('Введите слова через пробел: ').split()
    for word in words:
        print(int_func(word), end=' ')
    print()


ext_func()
