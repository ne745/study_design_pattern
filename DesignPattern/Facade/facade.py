# facade.py

class Knife:

    def __init__(self, name) -> None:
        self.__name = name

    def cut_vegetables(self):
        print(f'cut vegetables with {self.__name}.')


class Boiler:

    def __init__(self, name) -> None:
        self.__name = name

    def boil_vegetables(self):
        print(f'boil vegetables with {self.__name}.')


class Frier:

    def __init__(self, name) -> None:
        self.__name = name

    def fry_vegetables(self):
        print(f'fry vegetables with {self.__name}.')


# Facade
# システムを構成する様々なクラスを利用するためのクラス
class Cook:

    def __init__(self, knife: Knife, frier: Frier, boiler: Boiler):
        self.__knife = knife
        self.__frier = frier
        self.__boiler = boiler

    def cook_dish(self):
        self.__knife.cut_vegetables()
        self.__frier.fry_vegetables()
        self.__boiler.boil_vegetables()


knife = Knife('My Knife')
frier = Frier('My Frier')
boiler = Boiler('My Boiler')

cook = Cook(knife, frier, boiler)
cook.cook_dish()
# knife.cut_vegetables()
# boiler.boil_vegetables()
# frier.fry_vegetables()
