class Warehouse:
    def __init__(self, free_space):
        self.free_space = free_space


class OfficeEquipment:
    def __init__(self, brand, model, num, price):
        self.brand = brand
        self.model = model
        self.num = num
        self.price = price

class Printers(OfficeEquipment):
    def __init__(self,brand, model, num, price, cartridges):
        super().__init__(brand, model, num, price)
        self.cartridges = cartridges


class Copier(OfficeEquipment):
    def __init__(self,brand, model, num, price, cartridges, lamp):
        super().__init__(brand, model, num, price)
        self.cartridges = cartridges
        self.lamp = lamp


def __init__(self, brand, model, num, price, lamp):
    super().__init__(brand, model, num, price)
    self.lamp = lamp
