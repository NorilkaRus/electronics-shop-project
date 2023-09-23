from src.item import Item

class MixinKeyboard:
    LANGUAGE = "EN"

    def __init__(self):
        self.__language = "EN"
        MixinKeyboard.__language = self.__language


    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"


    @property
    def language(self):
        return self.__language


    @language.setter
    def language(self, lang):
        raise AttributeError("property 'language' of 'Keyboard' object has no setter")

class Keyboard(Item, MixinKeyboard):
    """
    Класс клавиатуры, наследуемый из класса товара + миксин с языками
    """
    pass

