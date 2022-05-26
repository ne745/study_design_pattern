# flyweight_2.py

# FlyWeightFactory
class FlyweightMixin:

    _instances = {}

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if (cls, *args) not in cls._instances:
            new_instance = cls(**kwargs)
            cls._instances[(cls, *args)] = new_instance
            return new_instance
        else:
            return cls._instances.get((cls, *args))


# FlyWeight
class User(FlyweightMixin):

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


# FlyWeight
class Car(FlyweightMixin):

    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model


user1 = User.get_instance(1, name='Taro', age=20)
user2 = User.get_instance(1)
print(id(user1))
print(id(user2))
print(user1.name)

car = Car.get_instance(1, brand='TOYOTA', model='Prius')
print(car.brand)
