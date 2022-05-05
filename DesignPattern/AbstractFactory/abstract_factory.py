# abstract_factory.py
from abc import ABC, abstractmethod


# Pdoduct
# 作成するオブジェクトの部品を定義するインターフェース
class AbcItem(ABC):

    def __init__(self, caption) -> None:
        self.caption = caption

    @abstractmethod
    def make_html(self):
        pass


# ConcreteProduct
# Product を具体化したクラス
class PageItem(AbcItem):

    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
        self.content = []

    def add(self, item):
        self.content.append(item)

    def write_html(self, filename):
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(self.make_html())


# ConcreteProduct
class LinkItem(AbcItem):
    # <a></a>

    def __init__(self, caption, url) -> None:
        super().__init__(caption)
        self.url = url


# ConcreteProduct
class ListItem(AbcItem):
    # <li></li>

    def __init__(self, caption) -> None:
        super().__init__(caption)
        self.items = []

    def add(self, item):
        self.items.append(item)


# Factory
# Product を生成する処理を定義したインターフェース
class Factory(ABC):

    @abstractmethod
    def create_page_item(self, title, author):
        pass

    @abstractmethod
    def create_link_item(self, caption, url):
        pass

    @abstractmethod
    def create_list_item(self, caption):
        pass
