# Задание 5.
class Stationery:
    title = 'прибор'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        print('Запуск отрисовки ручкой.')


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        print(f'Запуск отрисовки карандашем.')


class Handle(Stationery):
    title = 'Маркер'

    def draw(self):
        print('Запуск отрисовки маркером.')


stat = Stationery()
stat.draw()
pen_1 = Pen()
pen_1.draw()
pencil_1 = Pencil()
pencil_1.draw()
handle_1 = Handle()
handle_1.draw()
