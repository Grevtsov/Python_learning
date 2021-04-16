# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, \
# количества слов в каждой строке.


with open('text.txt') as f:
    contents = f.readlines()
    print(f'Количество строк в файле равно - {len(contents)}')
    for i, el in enumerate(contents, 1):
        print(f'{i}-я строка содержит {len(el.split())} слов(а)')
