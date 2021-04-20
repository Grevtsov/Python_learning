# Задание 2.
class Roads:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_wight(self, high, width_1sqm=25):
        print(f'Масса асфальта, необходимая для покрытия всего дорожного полотна равна'
              f' {self._length * self._width * width_1sqm * high / 1000:.0f} тон.')


a = Roads(20, 5000)
a.asphalt_wight(5)
