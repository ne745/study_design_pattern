# mediator.py
from abc import ABC, abstractmethod


# Colleague
# Mediator と通信して、処理を調整するインターフェース
class WindowBase(ABC):

    def __init__(self, mediator=None) -> None:
        self._mediator = mediator
        self._is_open = False

    @property
    def mediator(self):
        pass

    @mediator.getter
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator

    @property
    def is_open(self):
        pass

    @is_open.getter
    def is_open(self):
        return self._is_open

    @is_open.setter
    def is_open(self, is_open):
        self._is_open = is_open

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass


# ConcreteColleague
# Colleague を具体化したクラス
# Mediator によって処理を調整される
class MainWindow(WindowBase):

    def open(self):
        print('Open MainWindow')
        self.is_open = True

    def close(self):
        self.mediator.notify('main', 'close')
        print('Close MainWindow')
        self.is_open = False


# ConcreteColleague
class SettingsWindow(WindowBase):

    def open(self):
        self.mediator.notify('settings', 'open')
        print('Open SettingsWindow')
        self.is_open = True

    def close(self):
        print('Close SettingsWindow')
        self.is_open = False


# ConcreteColleague
class HelpWindow(WindowBase):

    def open(self):
        self.mediator.notify('help', 'open')
        print('Open HelpWindow')
        self.is_open = True

    def close(self):
        print('Close HelpWindow')
        self.is_open = False


# Mediator
# Colleague と通信を行い、処理の調整を行うインターフェース
class Mediator(ABC):

    @abstractmethod
    def notify(self, sender, action):
        pass


# ConcreteMediator
# Mediator を具体化したクラス
# 特定の Colleague に対しての調整を行う
class WindowMediator(Mediator):

    def __init__(self,
                 main_window: MainWindow,
                 settings_window: SettingsWindow,
                 help_window: HelpWindow) -> None:
        self.__main_window = main_window
        self.__settings_window = settings_window
        self.__help_window = help_window
        main_window.mediator = self
        settings_window.mediator = self
        help_window.mediator = self

    def notify(self, sender, action):
        if sender == 'settings' and action == 'open':
            if self.__help_window.is_open:
                self.__help_window.close()

        if sender == 'help' and action == 'open':
            if self.__settings_window.is_open:
                self.__settings_window.close()

        if sender == 'main' and action == 'close':
            if self.__help_window.is_open:
                self.__help_window.close()
            if self.__settings_window.is_open:
                self.__settings_window.close()


main_window = MainWindow()
settings_window = SettingsWindow()
help_window = HelpWindow()

mediator = WindowMediator(main_window, settings_window, help_window)

main_window.open()
settings_window.open()
help_window.open()
settings_window.open()
main_window.close()
