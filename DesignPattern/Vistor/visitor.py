# visitor.py
from abc import ABC, abstractmethod


# Element
# Visitor によって訪れられる対象となるクラスのインターフェースを定義
class ItemElement(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


# ConcreteElement
# Element を継承して具体的な処理を記述したクラス
class Book(ItemElement):

    def __init__(self, price, isbn) -> None:
        self.__price = price
        self.__isbn = isbn

    @property
    def price(self):
        pass

    @price.getter
    def price(self):
        return self.__price

    @property
    def isbn(self):
        pass

    @isbn.getter
    def isbn(self):
        return self.__isbn

    def accept(self, visitor):
        return visitor.visit(self)


# ConcreteElement
class Fruit(ItemElement):

    def __init__(self, price, weight, name) -> None:
        self.__price = price
        self.__weight = weight
        self.__name = name

    @property
    def price(self):
        pass

    @price.getter
    def price(self):
        return self.__price

    @property
    def weight(self):
        pass

    @weight.getter
    def weight(self):
        return self.__weight

    @property
    def name(self):
        pass

    @name.getter
    def name(self):
        return self.__name

    def accept(self, visitor):
        return visitor.visit(self)


# Visitor
# Element にアクセスするための抽象メソッドを定義
class Visitor(ABC):

    @abstractmethod
    def visit(self, item):
        pass


# ConcreteVisitor
# Visitor を継承したクラスで、具体的な処理を記述する
class ShoppingVisitor(Visitor):

    def visit(self, item: ItemElement):
        if isinstance(item, Book):
            cost = item.price
            if cost >= 50:
                cost -= 10
            print(f'Book ISBN: {item.isbn}, cost = {cost}')
            return cost
        elif isinstance(item, Fruit):
            cost = item.price * item.weight
            cost = int(cost * 0.8)
            print(f'{item.name}, cost = {cost}')
            return cost


def calcurate_price(items):
    visitor = ShoppingVisitor()
    sum_cost = 0
    for item in items:
        sum_cost += item.accept(visitor)
    return sum_cost


items = [
    Book(20, '1111'),
    Book(100, '2222'),
    Fruit(8, 10, 'Banana'),
    Fruit(10, 5, 'Apple')
]
print(f'Total cost = {calcurate_price(items)}')
