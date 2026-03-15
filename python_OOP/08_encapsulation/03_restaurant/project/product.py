class Product:
    def __init__(self, name, price):
        self.__name: str = name
        self.__price: str = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price
