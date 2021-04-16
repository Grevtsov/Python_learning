# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие \
# лекционных, практических и лабораторных занятий по этому предмету и их количество. \
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название \
# предмета и общее количество занятий по нему. Вывести словарь на экран.

from re import findall

with open(r'schedule.txt', 'r', encoding='utf-8') as f:
    schedule_dict = {}
    for line in f:
        schedule_dict.update({line.split(':')[0]: line.split(':')[1]})
for k, i in schedule_dict.items():
    schedule_dict[k] = sum(map(int, findall(r'\d+', i)))
    # print(k, i)
print(schedule_dict)
