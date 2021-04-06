result_list = (input('Введите значения элементов списка через пробел: ')).split()
print(f'Исходный список {result_list}')
for i in result_list:
    if result_list.index(i) % 2 == 0:
        position = result_list.index(i)
        print(position)
        tmp = result_list.pop(position)
        # print(result_list, tmp, position)
        result_list.insert(position + 1, tmp)
        # print(result_list)
print(f'Измененный список {result_list}')
