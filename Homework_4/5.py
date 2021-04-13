from functools import reduce


def my_dev(el, el_1):
    return el*el_1


my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(my_list)

print(reduce(my_dev, [el for el in my_list]))
