class Warehouse:

    def __init__(self, free_space):
        self.free_space = free_space


class OfficeEquipment:

    def __init__(self, brand, model, num, price):
        self.brand = brand
        self.model = model
        self.num = int(num)
        self.price = float(price)
        self.list_of_equipment = []
        self.current_object = {'Модель устройства': self.brand + self.model, 'Цена за ед': self.price,
                               'Количество': self.num}
        self.warehouse = []

    def transfer(self):

        try:
            object_name = input(f'Введите наименование товара ')
            object_price = float(input(f'Введите цену за ед '))
            object_num = int(input(f'Введите количество товара '))
            current_object = {'Модель устройства': object_name, 'Цена': object_price, 'Количество': object_num}
            self.current_object.update(current_object)
            self.warehouse.append(self.current_object)

        except:
            return f'Ошибка ввода данных. Цена за ед и кол-во должны быть числовыми, а название строкой'

        q = input('Для выхода - Q, для продолжения - Enter')
        if q == 'Q':
            return f'Весь склад - {self.warehouse}'

        else:
            OfficeEquipment.transfer(self)


class Printers(OfficeEquipment):
    def __init__(self, brand, model, num, price, cartridges):
        super().__init__(brand, model, num, price)
        self.cartridges = cartridges


class Copier(OfficeEquipment):

    def __init__(self, brand, model, num, price, cartridges, lamp):
        super().__init__(brand, model, num, price)
        self.cartridges = cartridges
        self.lamp = lamp


class Scanners(OfficeEquipment):

    def __init__(self, brand, model, num, price, lamp):
        super().__init__(brand, model, num, price)
        self.lamp = lamp
