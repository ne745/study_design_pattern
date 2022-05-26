# flyweight_1.py

# Flyweight
# 普通にインスタンスを作成するとメモリの使用量が大きいため、共有したほうが良いもの
class User:

    def __init__(self, name='', age='') -> None:
        self.__name = name
        self.__age = age

    @property
    def name(self):
        pass

    @name.getter
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        pass

    @age.getter
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self) -> str:
        return f'name: {self.__name}, age: {self.__age}'


# FlyWeightFactory
# Flyweight を作成する工場。
# FlyweightFactory を利用して Flyweight を作成するとオブジェクトが共有される
class UserFactory:

    __instances = {}

    @classmethod
    def get_instance(cls, user_id):
        if user_id not in cls.__instances:
            user = User()
            cls.__instances[user_id] = user
            return user
        return cls.__instances.get(user_id)


user1 = UserFactory.get_instance(1)
user1.name = 'Taro'
user1.age = 20

user2 = UserFactory.get_instance(2)
user3 = UserFactory.get_instance(1)

print(id(user1))
print(id(user2))
print(id(user3))

print(user3)
user3.name = 'Jiro'
print(user1)
