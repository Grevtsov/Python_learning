class ZeroDivisionCustom(Exception):
    def __init__(self, text='На ноль делить нельзя'):
        self.error_text = text

    def __str__(self):
        return f'ZeroDivisionError: На ноль делить нельзя!!!'


def zero_division(divisible, divisor):
    try:
        if divisor == 0:
            raise ZeroDivisionCustom
        else:
            return divisible / divisor
    except ZeroDivisionCustom as e:
        return e


if __name__ == '__main__':
    print(zero_division(10, 100))
    print(zero_division(10, 0))
