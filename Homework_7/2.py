from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.param + other.param


class Coat(Clothes):
    @property
    def consumption(self):
        return float(self.param / 6.5 + 0.5)

    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, param):
        if param < 40:
            self.__param = int(40)
        elif param > 60:
            self.param = int(60)
        else:
            self.param = param


class Suit(Clothes):
    @property
    def consumption(self):
        return float(self.param * 2 + 0.3)

    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, param):
        if param < 80:
            self.__param = int(80)
        elif param > 220:
            self.__param = int(220)
        else:
            self.__param = param


a = Coat(10)
b = Suit(50)
c = Suit(100)
print(a.param, b.param, c.param)
print(a+b)
