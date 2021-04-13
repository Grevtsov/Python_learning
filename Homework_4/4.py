my_list = [0, 2, 3, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 332, 4, 5 , 12, 20, 13, 14, 11]
my_new_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Уникальные элементы исходного списка: {my_new_list}')
