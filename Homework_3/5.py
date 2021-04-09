def sum_numbers(*args):
    """

    :return:
    """
    my_list_2 = []
    quite = False
    while quite == False:
        my_list = input('Введите числа через пробел или введите Q для выхода из программы: ')
        my_list = my_list.split()
        for el in my_list:
            print(el)
            if el != 'Q':
                my_list_2.append(float(el))
            elif el == 'Q':
                quite = True
        print(my_list_2)
    return (sum(my_list_2))


print(sum_numbers())
