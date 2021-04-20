# Задание 4.
from random import randrange


class Car:
    def __init__(self, speed, color, name, is_police=False, car_go=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.car_go = car_go

    def show_speed(self):
        print(f'Скорость {self.name} км/ч - {self.speed}')

    def go(self, car_go=True):
        self.car_go = car_go
        self.speed = randrange(10, 180)
        print(f'Машина {self.name} поехала')

    def stop(self, car_go=False):
        self.car_go = car_go
        self.speed = 0
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}.')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость {self.speed} км/ч. Автомобиль {self.name} цвет {self.color} - '
                  f'превышает скоростной режим!')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Текущая скорость {self.speed} км/ч. Автомобиль {self.name} цвет {self.color} - '
                  f'превышает скоростной режим!')


class SportCar(Car):
    def __init__(self, speed, color, name, sprt_car=True):
        super().__init__(speed, color, name)
        self.sport_car = sprt_car


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
        self.is_police = is_police


car = Car(50, 'red', 'Peugeot')
town_car = TownCar(70, 'blue', 'Kia')
work_car = WorkCar(42, 'green', 'Hyundai')
sport_car = SportCar(173, 'red', 'Maserati')
p_car = PoliceCar(100, 'black', 'Ford')
town_car.show_speed()
work_car.stop()
work_car.show_speed()
sport_car.turn('направо')
p_car.turn('налево')
print(f'Информация о Машине класса Car: марка - {car.name}, цвет - {car.color}, скорость в данный момент - {car.speed},'
      f' принадлежность к полиции - {car.is_police}, находится ли авто в движении - {car.car_go}\n'
      f'Информация о Машине класса TownCar: марка - {town_car.name}, цвет - {town_car.color}, '
      f'скорость в данный момент - {town_car.speed}, принадлежность к полиции - {town_car.is_police},'
      f' находится ли авто в движении - {town_car.car_go}\n'
      f'Информация о Машине класса WorkCar: марка - {work_car.name}, цвет - {work_car.color},'
      f'скорость в данный момент -  {work_car.speed}, принадлежность к полиции - {work_car.is_police},'
      f' находится ли авто в движении - {work_car.car_go}\n'
      f'Информация о Машине класса SportCar: марка - {sport_car.name}, цвет - {sport_car.color}, '
      f'скорость в данный момент - {sport_car.speed}, '
      f'принадлежность к полиции - {sport_car.is_police}, находится ли авто в движении -{sport_car.car_go}\n'
      f'Информация о Машине класса PoliceCar: марка - {p_car.name}, цвет - {p_car.color}, '
      f'скорость в данный момент - {p_car.speed}, принадлежность к полиции - {p_car.is_police}, '
      f'находится ли авто в движении -{p_car.car_go}')
