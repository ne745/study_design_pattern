# factory_method.py
from abc import ABC, abstractmethod


# Creator
# Product を生成する処理を定義したインターフェース
class IFactory(ABC):

    def __init__(self) -> None:
        self.registered_owners = []

    def create(self, owner):
        self._owner = owner
        product = self._create_product()
        self._register_product(product)
        return product

    @abstractmethod
    def _create_product(self):
        pass

    @abstractmethod
    def _register_product(self, product):
        pass


# ConcreteCreator
# Creator を具体化したクラス
class CarFactory(IFactory):

    def _create_product(self):
        return Car(self._owner)

    def _register_product(self, product):
        self.registered_owners.append(product.owner)


# ConcreteCreator
class ShipFactory(IFactory):

    def _create_product(self):
        return Ship(self._owner)

    def _register_product(self, product):
        self.registered_owners.append(product.owner)


# Product
# 作成するオブジェクトの構成要素を定義するインターフェース
class IProduct(ABC):

    def __init__(self, owner) -> None:
        self._owner = owner

    @abstractmethod
    def use(self):
        pass

    @abstractmethod
    def owner(self):
        pass


# ConcreteProduct
# Product を具体化したクラス
class Car(IProduct):

    def use(self):
        print(f'{self.owner}: driving car')

    @property
    def owner(self):
        pass

    @owner.getter
    def owner(self):
        return self._owner


# ConcreteProduct
class Ship(IProduct):

    def use(self):
        print(f'{self.owner}: piloting ship')

    @property
    def owner(self):
        pass

    @owner.getter
    def owner(self):
        return self._owner


car_factory = CarFactory()
yamada_car = car_factory.create('yamada')
sato_car = car_factory.create('sato')
yamada_car.use()
sato_car.use()
print(car_factory.registered_owners)

ship_factory = ShipFactory()
john_ship = ship_factory.create('john')
mike_ship = ship_factory.create('mike')
john_ship.use()
mike_ship.use()
print(ship_factory.registered_owners)
