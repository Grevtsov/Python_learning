user_text = input('Введите текст из нескольких слов: ').split()
for index, el in enumerate(user_text, 1):
    print('{} {:.10}' .format(index, el))
