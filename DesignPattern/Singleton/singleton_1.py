class DataBase():

    _instance = None

    def __init__(self) -> None:
        self.__database_url = None

    def __new__(cls):
        # インスタンス作成時に呼び出される特殊メソッド
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def database_url(self):
        pass

    @database_url.getter
    def database_url(self):
        return self.__database_url

    @database_url.setter
    def database_url(self, database_url):
        self.__database_url = database_url

    def connect(self):
        # Database に接続
        pass


a = DataBase()
b = DataBase()
print(a == b)
print(id(a))
print(id(b))
a.database_url = '128.1.1.1:5678'
print(a.database_url)
print(b.database_url)
