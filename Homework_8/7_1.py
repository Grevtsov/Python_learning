class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.complex_sum = 'a + b*i'

    def __str__(self):
        return f'{self.a} + {self.b}i'

    def __add__(self, other):
        return f'{self.a + other.a} + {self.a + other.b}i'

    def __mul__(self, other):
        return f'{self.a * other.a} + {self.a * other.b}i'


if __name__ == '__main__':
    v = ComplexNum(2, 5)
    k = ComplexNum(-1, 7)
    print(v)
    print(k)
    print(v+k)
    print(v*k)