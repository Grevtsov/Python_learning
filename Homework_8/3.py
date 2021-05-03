class ExceptionInt:
    def __init__(self):
        self.my_list = []

    def check_int(self):
        while True:
            try:
                val = input('Введите число. Чтобы завершить ввод введите "Q" ')
                if val == 'Q':
                    break
                self.my_list.append(int(val))

            except:
                print('Вы ввели недопустимое значение. Введите число или "Q" для завершения программы')
                val_2 = input('Введите число. Чтобы завершить ввод введите "Q" ')
                if val_2 == 'Q':
                    break
        return f'ваш список : {self.my_list}'

if __name__ == '__main__':
    b = ExceptionInt()
    print(b.check_int())
