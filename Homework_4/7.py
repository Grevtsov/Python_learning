from math import factorial
from itertools import count

def fact():
    for el in count(1):
        yield factorial(el)

generator = fact()
iter_num = 0
print(type(generator))
for i in generator:
    if iter_num <7:
        print(i)
        iter_num += 1
    else:
        break