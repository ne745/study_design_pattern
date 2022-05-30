# iterator2.py
from collections.abc import Iterator, Iterable


class Book:

    def __init__(self, name) -> None:
        self.__name = name

    def get_name(self):
        return self.__name


class BookShelf(Iterable):

    def __init__(self) -> None:
        self.__books = []

    def append_book(self, book: Book):
        self.__books.append(book)

    def get_book_at(self, index):
        return self.__books[index]

    # ルーブ分のときに Iterator として回してくれる
    def __iter__(self):
        print('iterator is created')
        return BookShelfIterator(self)

    def get_iterator(self):
        return BookShelfIterator(self)

    def get_reverse_iterator(self):
        return BookShelfIterator(self, reverse=True)


class BookShelfIterator(Iterator):

    def __init__(self, book_shelf: BookShelf, reverse=False) -> None:
        self.__book_shelf = book_shelf
        self.__index = -1 if reverse else 0
        self.__reverse = reverse

    def __next__(self):
        try:
            print(f'try: {self.__index}')
            book = self.__book_shelf.get_book_at(self.__index)
            self.__index += -1 if self.__reverse else 1
        except IndexError:
            # Iteratror.next が終了
            raise StopIteration()
        return book


book_shelf = BookShelf()
book_shelf.append_book(Book('Dragon Ball 1'))
book_shelf.append_book(Book('Dragon Ball 2'))
book_shelf.append_book(Book('Dragon Ball 3'))
book_shelf.append_book(Book('Dragon Ball 4'))

for book in book_shelf:
    print(book.get_name())

print('-' * 50)
book_iterator = book_shelf.get_iterator()
print(next(book_iterator).get_name())
print(next(book_iterator).get_name())
print(next(book_iterator).get_name())
print(next(book_iterator).get_name())

print('-' * 50)
book_reverse_iterator = book_shelf.get_reverse_iterator()
print(next(book_reverse_iterator).get_name())
print(next(book_reverse_iterator).get_name())
print(next(book_reverse_iterator).get_name())
print(next(book_reverse_iterator).get_name())
