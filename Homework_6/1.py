# Задание 1.
from time import sleep


class TrafficLight:
    __color = {'Красный': 7,
               'Желтый': 2,
               'Зелёный': 5
               }

    @staticmethod
    def running():
        for key, val in TrafficLight.__color.items():
            light = key
            print(light)
            sleep(val)


a = TrafficLight()
a.running()  # Проверка работы метода
a.running()  # Проверка работы метода
