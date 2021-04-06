print('Введите значения элементов списка по одному через нажатие клафиши "Enter"')
print('Как только закончите ввод всех элементов введите в строке "end"')
user_number = None
result_list = []
while True:
    user_number = input('Введите значение элементе списка: ')
    if user_number != 'end':
        result_list.append(user_number)
    else:
        break
print(f' исходный список {result_list}')
for i in result_list:
    if result_list.index(i) % 2 == 0:
        position = result_list.index(i)
        tmp = result_list.pop(position)
        result_list.insert(position + 1, tmp)
print(f' измененный список {result_list}')
