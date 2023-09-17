from csv import DictReader

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return self.__name


    def __add__(self, other):
        if isinstance(self, Item) and isinstance(other, Item):
            return self.quantity + other.quantity
        return None


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:9]


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.quantity * self.price
        return total_price


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate


    @classmethod
    def instantiate_from_csv(cls, file):
        Item.all = []
        with open(file, encoding='windows-1251') as file:
            dict_obj = DictReader(file)
            for row in dict_obj:
                __name = str(row['name'])
                price = float(row['price'])
                quantity = int(row['quantity'])
                item = cls(__name, price, quantity)


    @staticmethod
    def string_to_number(number_string):
        return int(float(number_string))