# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. \
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


while True:
    try:
        with open(r"sum_number.txt", "w+") as f:
            f.write(input('Введите числа через пробел: '))
            f.seek(0)
            print('Сумма всех чисел - {}'.format(sum(map(float, f.readline().split()))))
            break
    except ValueError:
        with open(r"sum_number.txt", "w+") as f:
            print('Ошибка ввода данных')
