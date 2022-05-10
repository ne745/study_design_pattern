# prototype.py
from abc import ABC, abstractmethod
from copy import deepcopy


# Prototype
# 複製するオブジェクトの構成要素を定義するインターフェース
class Prototype(ABC):

    @abstractmethod
    def use(self, msg):
        pass

    @abstractmethod
    def _clone(self):
        pass


# ConcretePrototype
# Prototype を具体化したクラス
class MessageBox(Prototype):

    def __init__(self, decoration_char) -> None:
        self.__decoration_char = decoration_char

    def use(self, msg):
        str_msg = str(msg)
        print(self.__decoration_char * (len(str_msg) + 4))
        print(
            self.__decoration_char + ' ' +
            str_msg +
            ' ' + self.__decoration_char
        )
        print(self.__decoration_char * (len(str_msg) + 4))

    def _clone(self):
        print('MessageBox のクローンを作成します')
        return deepcopy(self)

    @property
    def decoration_char(self):
        pass

    @decoration_char.getter
    def decoration_char(self):
        return self.__decoration_char

    @decoration_char.setter
    def decoration_char(self, decoration_char):
        self.__decoration_char = decoration_char


# ConcretePrototype
class UnderlinePen(Prototype):

    def __init__(self, underline_char) -> None:
        self.__underline_char = underline_char

    def use(self, msg):
        str_msg = str(msg)
        print(str_msg)
        print(self.__underline_char * len(str_msg))

    def _clone(self):
        print('UnderlinePen のコピーを作成します')
        return deepcopy(self)

    @property
    def underline_char(self):
        pass

    @underline_char.getter
    def underline_char(self):
        return self.__underline_char

    @underline_char.setter
    def underline_char(self, underline_char):
        self.__underline_char = underline_char


# Manager
# ConcretePrototype を登録し複製を作成するクラス
class Manager:

    def __init__(self) -> None:
        self.__products = {}

    def register(self, name, prototype: Prototype):
        self.__products[name] = deepcopy(prototype)

    def create_product(self, name):
        product = self.__products.get(name)
        return product._clone()


m_box = MessageBox('*')
m_box.use('Hello')

u_pen = UnderlinePen('-')
u_pen.use('Hello')

manager = Manager()
manager.register('message_box', m_box)
manager.register('underline_pen', u_pen)

new_m_box = manager.create_product('message_box')
new_m_box.use('New box')

m_box.decoration_char = '='
m_box.use('Hello')
m_box_clone = manager.create_product('message_box')
m_box_clone.use('Hello2')
