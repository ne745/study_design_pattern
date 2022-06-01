# strategy.py
from abc import ABC, abstractmethod
from enum import Enum
from random import randint


class Hand_Type(Enum):
    GUU = 0
    CHOKI = 1
    PAA = 2


class Hand:

    def __init__(self, hand_index) -> None:
        if hand_index not in (0, 1, 2):
            raise Exception('value is wrong')
        self.hand_index = hand_index

    def is_win(self, other):
        if any((
            (self.hand_index == Hand_Type.GUU.value and
             other.hand_index == Hand_Type.CHOKI.value),
            (self.hand_index == Hand_Type.CHOKI.value and
             other.hand_index == Hand_Type.PAA.value),
            (self.hand_index == Hand_Type.PAA.value and
             other.hand_index == Hand_Type.GUU.value),
        )):
            return True
        return False

    def is_lose(self, other):
        if any((
            (self.hand_index == Hand_Type.GUU.value and
             other.hand_index == Hand_Type.PAA.value),
            (self.hand_index == Hand_Type.CHOKI.value and
             other.hand_index == Hand_Type.GUU.value),
            (self.hand_index == Hand_Type.PAA.value and
             other.hand_index == Hand_Type.CHOKI.value),
        )):
            return True
        return False


# Strategy
# 戦略を利用するためのインターフェース
class Strategy(ABC):

    @abstractmethod
    def next_hand(self):
        pass

    @abstractmethod
    def study(self, is_win):
        pass


# ConcreteStrategy
# Strategy を具体化したクラスで、様々な戦略を表現する
class SimpleStrategy(Strategy):

    def __init__(self) -> None:
        self.hand = None
        self.is_win = False

    def next_hand(self):
        if not self.is_win:
            self.hand = Hand(randint(0, 2))
        return self.hand

    def study(self, is_win):
        self.is_win = is_win


# ConcreteStrategy
class ComplexStrategy(Strategy):

    def __init__(self) -> None:
        self.current_hand = None
        self.previous_hand = None
        self.histories = [
            [0, 0, 0],  # previous GUU
            [0, 0, 0],  # previous CHOKI
            [0, 0, 0]   # previous PAA
            # ^  ^  ^ current
            # |  |  |
            # |  |  PAA
            # |  CHOKI
            # GUU
        ]

    def next_hand(self):
        if self.current_hand:
            self.previous_hand = self.current_hand
        self.current_hand = self.__get_most_winning_hand()
        return self.current_hand

    def __get_most_winning_hand(self):
        if not self.previous_hand:
            return Hand(randint(0, 2))
        temp_hand = 0
        prev = self.previous_hand.hand_index
        if self.histories[prev][1] > self.histories[prev][temp_hand]:
            temp_hand = 1
        if self.histories[prev][2] > self.histories[prev][temp_hand]:
            temp_hand = 2
        return Hand(temp_hand)

    def study(self, is_win):
        if not self.previous_hand:
            return
        if is_win:
            prev = self.previous_hand.hand_index
            curr = self.current_hand.hand_index
            self.histories[prev][curr] += 1
        else:
            prev = self.previous_hand.hand_index
            curr = (self.current_hand.hand_index + 1) % 3
            self.histories[prev][curr] += 1
            prev = self.previous_hand.hand_index
            curr = (self.current_hand.hand_index + 2) % 3
            self.histories[prev][curr] += 1


# Context
# 状況に応じて戦略を設定して実行するためのクラス
class Player:

    def __init__(self, name, strategy: Strategy) -> None:
        self.name = name
        self.strategy = strategy
        self.win_count = 0
        self.lose_count = 0
        self.game_count = 0

    def next_hand(self):
        return self.strategy.next_hand()

    def win(self):
        self.strategy.study(True)
        self.win_count += 1
        self.game_count += 1

    def lose(self):
        self.strategy.study(False)
        self.lose_count += 1
        self.game_count += 1

    def even(self):
        self.game_count += 1

    def __str__(self) -> str:
        out = f"{self.name}: "
        out += f"{self.game_count} games, "
        out += f"{self.win_count} wins, "
        out += f"{self.lose_count} lose"
        return out


taro = Player('Taro', SimpleStrategy())
jiro = Player('Jiro', ComplexStrategy())
for _ in range(10000):
    taro_hand = taro.next_hand()
    jiro_hand = jiro.next_hand()
    if taro_hand.is_win(jiro_hand):
        taro.win()
        jiro.lose()
    elif taro_hand.is_lose(jiro_hand):
        taro.lose()
        jiro.win()
    else:
        taro.even()
        jiro.even()

print(taro)
print(jiro)
