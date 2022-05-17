# bridge.py
from abc import ABC, abstractmethod


# Implementer
# 基本的な機能を記述したインターフェース
class Shape(ABC):

    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height

    @abstractmethod
    def create_shape_str(self):
        pass


# ConcreteImplementer
# Implementer を継承して処理を具体的に記述するクラス
class RectangleShape(Shape):

    def __init__(self, width, height) -> None:
        super().__init__(width, height)

    def create_shape_str(self):
        rectangle = '*' * self._width + '\n'
        for _ in range(self._height - 2):
            rectangle += '*' + ' ' * (self._width - 2) + '*' + '\n'
        rectangle += '*' * self._width + '\n'
        return rectangle


# ConcreteImplementer
class SquareShape(Shape):

    def __init__(self, width, height=None) -> None:
        super().__init__(width, width)

    def create_shape_str(self):
        square = '*' * self._width + '\n'
        for _ in range(self._width - 2):
            square += '*' + ' ' * (self._width - 2) + '*' + '\n'
        square += '*' * self._width + '\n'
        return square


# Abstraction
# 追加として実装される機能を Implementer と切り離して作成する処理を記述した抽象クラス
class WriteAbstraction(ABC):

    def __init__(self, shape: Shape) -> None:
        self._shape = shape

    def read_shape(self):
        return self._shape.create_shape_str()

    @abstractmethod
    def write_to_text(self, filename):
        pass


# RefinedAbstraction
# Abstraction の処理を具体的に記述したクラス
class WriteShape(WriteAbstraction):

    def write_to_text(self, filename):
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(self.read_shape())


rectangle = RectangleShape(10, 5)
# print(rectangle.create_shape_str())
square = SquareShape(5, 5)
# print(square.create_shape_str())
write_shape = WriteShape(square)
write_shape.write_to_text('tmp.txt')
