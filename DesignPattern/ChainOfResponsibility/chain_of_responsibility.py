# chain_of_responsibility.py
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
    gender: str


# Handler
# 要求を処理するインターフェース
# 自分自身のインスタンスを持つ
class Handler(ABC):

    _next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    def handle(self, user: User):
        # filter が True の場合処理を抜ける
        if self.filter(user):
            return self.done(user)
        # next が存在する場合は　 next の handle を実行
        if self._next:
            return self._next.handle(user)
        return self.end(user)

    @abstractmethod
    def filter(self, user: User):
        pass

    def done(self, user: User):
        print(f'{user} is filtered by {self.__class__.__name__}.')
        return False

    def end(self, user: User):
        print(f'{user} confirmation is completed.')
        return True


# ConcreteHandler
# 自分で処理できる場合は処理し、
# 処理できない場合は別のクラスに処理を回す
class NameCheckHandler(Handler):

    def filter(self, user: User):
        if user.name in ['', None]:
            return True
        return False


# ConcreteHandler
class AgeCheckHandler(Handler):

    def filter(self, user: User):
        if (user.age < 0) or (user.age > 100):
            return True
        return False

    def done(self, user: User):
        print('Age must be more than 0 or less than 100.')


# ConcreteHandler
class GenderCheckHandler(Handler):

    def filter(self, user: User):
        if user.gender not in ['Man', 'Woman']:
            return True
        return False


name_handler = NameCheckHandler()
age_handler = AgeCheckHandler()
gender_handler = GenderCheckHandler()
name_handler.set_next(age_handler).set_next(gender_handler)

user1 = User('Taro', 20, 'Man')
name_handler.handle(user1)

user2 = User('A', 101, '')
name_handler.handle(user2)

user1 = User('Taro', 20, 'M')
user2 = User('Taro', 20, 'Man')
user3 = User('', 20, 'Man')
user4 = User('Taro', 120, 'Man')
user5 = User('Taro', 20, 'Woman')

valid_users = []
for user in [user1, user2, user3, user4, user5]:
    if name_handler.handle(user):
        valid_users.append(user)
print(valid_users)
