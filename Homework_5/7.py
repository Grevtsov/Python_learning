# . Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма \
# собственности, выручка, издержки. # Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также \
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать. Далее реализовать список. \
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила \
# убытки, также добавить ее в словарь (со значением убытков).

import json
com_prof = {}
i = 0
plus_prof = 0
with open(r'companies.txt', 'r', encoding='utf-8') as f:
    for line in f:
        com_prof.update({line.split()[0]: float(line.split()[2]) - float(line.split()[3])})

for value in com_prof.values():
    if value > 0:
        plus_prof = plus_prof + value
        i += 1
avg_prof = {
    "average_profit": plus_prof / i
}
com_prof_list = [com_prof, avg_prof]
print(com_prof_list)
with open("companies_profit.json", "w") as j:
    json.dump(com_prof_list, j)
