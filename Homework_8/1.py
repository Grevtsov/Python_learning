class Date:
    def __init__(self, arg):
        self.date = arg

    @classmethod
    def int_date(cls, arg):
        date = []
        for i in arg.split('-'):
            date.append(int(i))
        return date

    @staticmethod
    def validation(arg):
        date = str(arg).split('-')
        if 1 <= int(date[0]) <= 31:
            if 1 <= int(date[1]) <= 12:
                if 2019 >= int(date[2]) >= 0:
                    return f'All right'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Введена дата: {Date.int_date(self.date)[0]} - {Date.int_date(self.date)[1]}' \
               f' - {Date.int_date(self.date)[2]}'


if __name__ == "__main__":
    print(Date.int_date('20-12-2021'))
    d = Date('20-12-2021')
    print(d.int_date('20-12-2021'))
    print(d.validation('20-12-2021'))
    today = Date('11 - 1 - 2001')
    print(today)
    print(Date.validation('11-11-2022'))
    print(today.validation('11 - 1 - 2001'))
    print(Date.validation('41-11-2000'))
