my_list = [1, 2, 1, 2, 16, 5, 7, 5, 2, 8, 9, 3, 1, 9, 6]
number = input('Введите натуральное число: ')
while not number.isdigit() or int(number) <= 0:
    number = (input('Введите натуральное число: '))
number = int(number)
my_list.append(number)
my_list = sorted(my_list, reverse=True)
print(my_list)
