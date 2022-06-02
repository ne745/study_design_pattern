# template_method.py
from abc import ABC, abstractmethod


# AbstractClass
# 外部から実行されるテンプレートメソッドを実装し、
# テンプレートメソッドの中で利用される抽象メソッドを宣言する
class AbstractDisplay(ABC):

    def display(self):
        self._open()
        for _ in range(5):
            self._print()
        self._close()
        self._additional_method()

    @abstractmethod
    def _open(self):
        pass

    @abstractmethod
    def _print():
        pass

    @abstractmethod
    def _close(self):
        pass

    def _additional_method(self):
        pass


# ConcreteClass
# AbstractClass を継承して、抽象メソッドを定義する
class CharDisplay(AbstractDisplay):

    def __init__(self, character) -> None:
        self.__character = character

    def _open(self):
        print('<<', end='')

    def _print(self):
        print(self.__character, end='')

    def _close(self):
        print('>>')

    def _additional_method(self):
        print('Additional method called')


# ConcreteClass
class StringDisplay(AbstractDisplay):

    def __init__(self, msg) -> None:
        self.__msg = msg

    def _open(self):
        self.__print_line()

    def _print(self):
        print('|' + self.__msg + '|')

    def _close(self):
        self.__print_line()

    def __print_line(self):
        print('+' + '-' * len(self.__msg) + '+')


c_display = CharDisplay('*')
c_display.display()

s_display = StringDisplay('Hello')
s_display.display()
