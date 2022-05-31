# state.py
from abc import ABC, abstractmethod
from datetime import datetime


# State
# 状態を表し、状態ごとに異なる振る舞いをする
class State(ABC):

    @abstractmethod
    def begin(self):
        pass

    @abstractmethod
    def write_log(self):
        pass

    @abstractmethod
    def end(self):
        pass


# ConcreteState
# State を具体化したクラスで、個々の状態を表現する
class DayState(State):

    def begin(self):
        print('start afternoon process')

    def write_log(self):
        with open('temp.txt', mode='w', encoding='utf-8') as f:
            f.write('log of day')

    def end(self):
        print('end afternoon process')


# ConcreteState
class NightState(State):

    def begin(self):
        print('start night process')

    def write_log(self):
        with open('temp.txt', mode='w', encoding='utf-8') as f:
            f.write('log of night')

    def end(self):
        print('end night process')


# Context
# 現在の状態を表す ConcreteState をもち、State パターン利用に必要な処理を表現
class Context:

    def __init__(self) -> None:
        self.__state = DayState()

    def do(self):
        self.change_state_by_time()
        self.__state.begin()
        self.__state.write_log()
        self.__state.end()

    def change_state(self, state: State):
        self.__state = state

    def change_state_by_time(self):
        now = datetime.now()
        if now.hour < 6 or 19 <= now.hour:
            self.__state = NightState()
        else:
            self.__state = DayState()


context = Context()
context.do()
