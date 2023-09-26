from src.item import Item
from settings import ITEMS_CSV

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv(ITEMS_CSV)
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(ITEMS_CSV)
    # InstantiateCSVError: Файл item.csv поврежден
