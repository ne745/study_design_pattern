# Builder パターン
from abc import ABC, abstractmethod, abstractproperty


# Product
# Builder によって作成されるオブジェクト
class SetMeal:

    @property
    def main_dish(self):
        pass

    @main_dish.getter
    def main_dish(self):
        return self.__main_dish

    @main_dish.setter
    def main_dish(self, main_dish):
        self.__main_dish = main_dish

    @property
    def side_dish(self):
        pass

    @side_dish.getter
    def side_dish(self):
        return self.__side_dish

    @side_dish.setter
    def side_dish(self, side_dish):
        self.__side_dish = side_dish

    def __str__(self) -> str:
        return f'main: {self.main_dish}, side: {self.side_dish}'


# Bulder
# Product を作成する処理を記述したインターフェース
class SetMealBuilder(ABC):

    def __init__(self) -> None:
        self._set_meal = SetMeal()

    @abstractproperty
    def product(self):
        pass

    @abstractmethod
    def build_main_dish(self):
        pass

    @abstractmethod
    def build_side_dish(self):
        pass


# ConcreteBuilder
# Builder の処理を具体化したクラス
class SanmaSetBuilder(SetMealBuilder):

    def __init__(self) -> None:
        super().__init__()

    @property
    def product(self):
        pass

    @product.getter
    def product(self):
        return self._set_meal

    def build_main_dish(self):
        self._set_meal.main_dish = 'sanma'

    def build_side_dish(self):
        self._set_meal.side_dish = 'omisoshiru'


# ConcreteBuilder
class PastaSetBuilder(SetMealBuilder):

    def __init__(self) -> None:
        super().__init__()

    @property
    def product(self):
        pass

    @product.getter
    def product(self):
        return self._set_meal

    def build_main_dish(self):
        self._set_meal.main_dish = 'pasta'

    def build_side_dish(self):
        self._set_meal.side_dish = 'soup'


# Director
# Builder を利用するクラス
class Director:

    def __init__(self, builder: SetMealBuilder) -> None:
        self.__builder = builder

    @property
    def builder(self):
        pass

    @builder.getter
    def builder(self):
        return self.__builder

    @builder.setter
    def builder(self, builder):
        self.__builder = builder

    def build(self):
        self.builder.build_main_dish()
        self.builder.build_side_dish()


sanma_builder = SanmaSetBuilder()
director = Director(sanma_builder)
director.build()
print(director.builder.product)

pasta_builder = PastaSetBuilder()
director = Director(pasta_builder)
director.build()
print(director.builder.product)
