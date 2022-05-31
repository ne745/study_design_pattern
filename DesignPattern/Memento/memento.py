# memento.py
from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime
import pickle


# Originator
# Memento を用いて、オブジェクトの状態を保存する
class Originator:

    def __init__(self, state, name) -> None:
        self._state = state
        self._name = name

    def change_state(self, new_state):
        print(f'change state: {new_state}')
        self._state = new_state

    def change_name(self, new_name):
        print(f'change name: {new_name}')
        self._name = new_name

    def __str__(self) -> str:
        return f'state: {self._state}, name: {self._name}'

    def save(self):
        return ConcreteMemento(self._state, self._name)

    def restore(self, memento):
        self._state = memento.state
        self._name = memento.name
        print(f'Originator: state change to {self._state}')


# Memento
# オブジェクトの状態の保存を行うインターフェース
class Memento(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractproperty
    def date(self):
        pass


# ConcreteMemento
# Memento を具体化したクラス
# 特定の Originator の状態を保存する
class ConcreteMemento(Memento):

    def __init__(self, state, name) -> None:
        self._state = state
        self._name = name
        self._date = datetime.now()

    @property
    def state(self):
        pass

    @state.getter
    def state(self):
        return self._state

    @property
    def name(self):
        pass

    @name.getter
    def name(self):
        return self._name

    @property
    def date(self):
        pass

    @date.getter
    def date(self):
        return self._date

    def get_name(self):
        return f'{self.date} / ({self.state})'


# CareTaker
# 特定の Originator のバックアップやもとに戻すなどの処理を行う
class CareTaker:

    def __init__(self) -> None:
        self._mementos = []

    def backup(self, memento: Memento):
        print(f'save state of Original: {memento.get_name()}')
        self._mementos.append(memento)

    def undo(self):
        if not len(self._mementos):
            return
        memento = self._mementos.pop()
        return memento

    def show_history(self):
        print('history')
        for memento in self._mementos:
            print(memento.get_name())


class OriginatorBackup:

    @staticmethod
    def dump_file(originator, filename):
        with open(filename, mode='wb') as f:
            pickle.dump(originator, f)

    @staticmethod
    def load_file(filename):
        with open(filename, mode='rb') as f:
            return pickle.load(f)


originator = Originator('FirstState', 'Originator1')
care_taker = CareTaker()
backup_instance = originator.save()
care_taker.backup(backup_instance)

originator.change_state('SecondState')
originator.change_name('NewOriginator1')
backup_instance = originator.save()
care_taker.backup(backup_instance)

originator.change_state('ThirdState')
originator.change_name('NewOriginator2')
print(originator)
undo_instance = care_taker.undo()
originator.restore(undo_instance)
print(originator)

# OriginatorBackup.dump_file(originator, 'temp.dump')
originator2 = OriginatorBackup.load_file('temp.dump')
print(originator2)
print(type(originator2))
