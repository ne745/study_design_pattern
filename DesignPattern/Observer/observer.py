# observer.py
from abc import ABC, abstractmethod
from random import randint


# Subject
# 観察される側
# Observer を登録したり削除する処理
class Subject(ABC):

    def __init__(self) -> None:
        self._number = 0
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    @abstractmethod
    def notify(self):
        # Observer を呼び出す
        pass

    @abstractmethod
    def execute(self):
        pass


# ConcreteSubject
# Subject を継承して処理を具体化したクラス
class NumberSubject(Subject):

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def change_value(self):
        number = self._number
        self._number = randint(0, 20)
        print(f'number change from {number} to {self._number}')
        self.notify()

    def execute(self):
        print('NumberSubject called')


# Observer
# 観察者で Subject から呼び出され、特定の処理を実行
class Observer(ABC):

    @abstractmethod
    def update(self, subject: Subject):
        pass


# ConcreteObserver
# Observer を具体化したクラス
class GraphObserver(Observer):

    def update(self, subject: Subject):
        print('GraphObserver: ' + '*' * subject._number)
        subject.execute()


class NumberObserver(Observer):

    def update(self, subject: Subject):
        print('NumberObserver: ' + str(subject._number))
        subject.execute()


subject = NumberSubject()
graph_observer = GraphObserver()
number_observer = NumberObserver()

subject.attach(graph_observer)
subject.attach(number_observer)
subject.change_value()

print('-' * 50)
subject.detach(graph_observer)
subject.change_value()
