# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские \
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


with open(r'numbers.txt', 'r', encoding='utf-8') as f:
    my_dict = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре'
    }
    # print(my_dict.get('One'))
    for line in f:
        rep_line = line.replace(line.split()[0], my_dict.get(line.split()[0]))
        with open(r'number_replaced.txt', 'a') as f_rep:
            f_rep.write(rep_line)
with open(r'number_replaced.txt') as f_rep:
    print(f_rep.readlines())
