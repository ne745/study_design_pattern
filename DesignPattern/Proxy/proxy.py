# proxy.py

from abc import ABC, abstractmethod
import time


# Subject
# RealSubject と Proxy を同一視して利用するためのインターフェース
class APICaller(ABC):

    @abstractmethod
    def request(self):
        pass


# RealSubject
# Subject を継承して処理を記述する
class RealAPICaller(APICaller):

    # 処理の重いコンストラクタとする
    def __init__(self, url) -> None:
        self.__url = url
        time.sleep(5)

    def request(self):
        print('Call API')


# Proxy
# RealSubject の代わりにクライアントからの処理を返す
# 自分で処理ができなかった場合に RealSubject を呼び出す
class RealAPICallerProxy(APICaller):

    def __init__(self, url) -> None:
        self.__url = url

    def __check_access(self):
        print('Successfully access')
        return True

    def __write_log(self):
        print('Output logs')

    def request(self):
        if self.__check_access():
            real_api_caller = RealAPICaller(self.__url)
            real_api_caller.request()
            self.__write_log()


# caller = RealAPICaller('http://hoge.com')
# caller.request()

proxy = RealAPICallerProxy('http://hoge.com')
proxy.request()
