# decorator.py
from abc import ABC, abstractmethod


# Component
# 機能を追加する際の中核となるクラス
class Component(ABC):

    @abstractmethod
    def operation(self):
        pass


# ConcreteComponent
# 追加する処理を記載した　Component を継承したクラス
class ShowCharComponent(Component):

    def __init__(self, char) -> None:
        self.__char = char

    def operation(self):
        print(self.__char * 20)


# Decorator
# Component を継承したクラスでプロパティに Component を持つ
class ShowDecorator(Component):

    def __init__(self, component: Component) -> None:
        self._component = component


# ConcreteDecorator
# Decorator の処理を具体的に記述したクラス
class ShowMessage(ShowDecorator):

    def __init__(self, component: Component, msg) -> None:
        super().__init__(component)
        self.__msg = msg

    def operation(self):
        self._component.operation()
        print(self.__msg)
        self._component.operation()


# Decorator
class WriteDecorator(Component):

    def __init__(self, component: Component, filename, msg) -> None:
        self._component = component
        self._filename = filename
        self._msg = msg


# ConcreteDecorator
class WriteMessage(WriteDecorator):

    def operation(self):
        self._component.operation()
        with open(self._filename, mode='w') as f:
            f.write(self._msg)


show_component = ShowCharComponent('-')
show_message = ShowMessage(show_component, 'Hello World')
# show_message.operation()
write_message = WriteMessage(show_message, 'tmp.txt', 'Write Message')
write_message.operation()
