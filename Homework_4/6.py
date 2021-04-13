# а) итератор, генерирующий целые числа, начиная с указанного,

from itertools import count

num = int(input('Введите начало стартовое число: '))
i = 0
for el in count(num):
    if i > 10:
        break
    else:
        print(el)
    i += 1

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import cycle

my_list =['Gibson', 'Fender', 'PRS', 'Jacson']
iter = cycle(my_list)
с = 0
while с < 10:
    print(next(iter))
    с += 1
