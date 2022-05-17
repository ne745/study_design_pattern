# composite.py
from abc import ABC, abstractproperty


# Component
# Composite と Leaf の共通機能を持った抽象クラス
class Component(ABC):

    @abstractproperty
    def name(self):
        pass

    @abstractproperty
    def size(self):
        pass

    @property
    def parent(self):
        pass

    @parent.getter
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def __str__(self) -> str:
        return f'{self.name} ({self.size})'


# Leaf
# 中身を表す役のクラス。この中には要素を入れることはできない
class File(Component):

    def __init__(self, name, size) -> None:
        self.__name = name
        self.__size = size
        self._parent = None

    @property
    def name(self):
        pass

    @name.getter
    def name(self):
        return self.__name

    @property
    def size(self):
        pass

    @size.getter
    def size(self):
        return self.__size

    # 自分のパスと名前を表示
    def print_list(self, path=''):
        print(path + '/' + str(self))


# Composite
# 容器を表す役を持ったクラスで、
# この中に Composite, Leaf を入れていき、階層構造を作成する
class Directory(Component):

    def __init__(self, name) -> None:
        self.__name = name
        self.__children = {}
        self._parent = None

    @property
    def name(self):
        pass

    @name.getter
    def name(self):
        return self.__name

    @property
    def size(self):
        pass

    @size.getter
    def size(self):
        file_size = 0
        for child in self.__children:
            file_size += self.__children[child].size
        return file_size

    def add_child(self, child):
        self.__children[child.name] = child
        child.parent = self

    def remove_child(self, child):
        if child.name in self.__children:
            del self.__children[child.name]
            child.parent = None

    def print_list(self, path=''):
        print(path + '/' + str(self))
        for child in self.__children:
            self.__children[child].print_list(path + '/' + self.name)


file1 = File('tmp1.txt', 1000)
file2 = File('tmp2.txt', 2000)
file3 = File('tmp3.txt', 3000)
file4 = File('tmp4.txt', 4000)

root_dir = Directory('root')
home_dir = Directory('home')
sys_dir = Directory('sys')
taro_dir = Directory('taro')

root_dir.add_child(home_dir)
root_dir.add_child(sys_dir)

home_dir.add_child(taro_dir)
home_dir.add_child(file3)

taro_dir.add_child(file1)
taro_dir.add_child(file2)

sys_dir.add_child(file4)
sys_dir.remove_child(file4)

root_dir.print_list()
