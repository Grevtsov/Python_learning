day_num = 1
first_day_result = float(input('Сколько километров Вы пробежали в первый день? '))
desired_result = float(input('Желаемый результат? '))
if first_day_result >= desired_result:
    print('В {} день результат: {:.2f} км'.format(day_num, first_day_result))
else:
    print('В {} день результат: {:.2f} км'.format(day_num, first_day_result))
    while first_day_result < desired_result:
        first_day_result = first_day_result + first_day_result * 0.1
        day_num += 1
        print('В {} день результат: {:.2f} км'.format(day_num, first_day_result))
print('В {} день спортсмен достиг результата — не менее {} км'.format(day_num, desired_result))
