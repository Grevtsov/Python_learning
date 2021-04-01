number = int(input('Введите целое положительное число: '))
while number <= 0:
    number = int(input('Введите целое положительное число: '))
max_number = number % 10
while number >= 1:
    number = number // 10
    if number % 10 > max_number:
        max_number = number % 10
print('Самая большая цифра в числе: ' + str(max_number))
