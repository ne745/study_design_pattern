from abc import ABC, abstractmethod
from enum import Enum


class CommandNumber(Enum):

    LIGHT = 0
    TV = 1
    GAME = 2


# Reciever
# Command が命令を実行する際の対象となるクラス
class Tv:

    def __init__(self, name) -> None:
        self.__name = name

    def turn_on_tv(self):
        print(f'TV: {self.__name} is turned on.')

    def turn_off_tv(self):
        print(f'TV: {self.__name} is turned off.')


# Reciever
class Light:

    def __init__(self, name) -> None:
        self.__name = name

    def turn_on_light(self):
        print(f'Light: {self.__name} is turned on.')

    def turn_off_light(self):
        print(f'Light: {self.__name} is turned off.')


# Reciever
class Game:

    def __init__(self, name) -> None:
        self.__name = name

    def turn_on_game(self):
        print(f'Game: {self.__name} is turned on.')

    def turn_off_game(self):
        print(f'Game: {self.__name} is turned off.')


# Command
# 命令を定義したインターフェース
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# ConcreteCommand
# Command を具体化したもの
# Reviever を扱う命令を記述する
class NoCommand(Command):

    def execute(self):
        pass

    def undo(self):
        pass


# ConcreteCommand
class LightTurnOnCommand(Command):

    def __init__(self, light: Light) -> None:
        self.__light = light

    def execute(self):
        self.__light.turn_on_light()

    def undo(self):
        self.__light.turn_off_light()


# ConcreteCommand
class LightTurnOffCommand(Command):

    def __init__(self, light: Light) -> None:
        self.__light = light

    def execute(self):
        self.__light.turn_off_light()

    def undo(self):
        self.__light.turn_on_light()


# ConcreteCommand
class TvTurnOnCommand(Command):

    def __init__(self, tv: Tv) -> None:
        self.__tv = tv

    def execute(self):
        self.__tv.turn_on_tv()

    def undo(self):
        self.__tv.turn_off_tv()


# ConcreteCommand
class TvTurnOffCommand(Command):

    def __init__(self, tv: Tv) -> None:
        self.__tv = tv

    def execute(self):
        self.__tv.turn_off_tv()

    def undo(self):
        self.__tv.turn_on_tv()


# ConcreteCommand
class GameTurnOnCommand(Command):

    def __init__(self, game: Game) -> None:
        self.__game = game

    def execute(self):
        self.__game.turn_on_game()

    def undo(self):
        self.__game.turn_off_game()


# ConcreteCommand
class GameTurnOffCommand(Command):

    def __init__(self, game: Game) -> None:
        self.__game = game

    def execute(self):
        self.__game.turn_off_game()

    def undo(self):
        self.__game.turn_on_game()


# Invoker
# 命令を実行する役目のクラス
class RemoteController:

    def __init__(self) -> None:
        self.__on_commands = [NoCommand()] * len(CommandNumber)
        self.__off_commands = [NoCommand()] * len(CommandNumber)
        self.__undo_command = NoCommand()

    def set_command(self, number,
                    turn_on_command: Command, turn_off_command: Command):
        self.__on_commands[number] = turn_on_command
        self.__off_commands[number] = turn_off_command

    def turn_on_command(self, number):
        self.__on_commands[number].execute()
        self.__undo_command = self.__on_commands[number]

    def turn_off_command(self, number):
        self.__off_commands[number].execute()
        self.__undo_command = self.__off_commands[number]

    def undo_command(self):
        self.__undo_command.undo()


light = Light('My Light')
tv = Tv('REGZA')
game = Game('Nintendo')

light_turn_on_command = LightTurnOnCommand(light)
light_turn_off_command = LightTurnOffCommand(light)

tv_turn_on_command = TvTurnOnCommand(tv)
tv_turn_off_command = TvTurnOffCommand(tv)

game_turn_on_command = GameTurnOnCommand(game)
game_turn_off_command = GameTurnOffCommand(game)

remote_controller = RemoteController()
remote_controller.set_command(
    CommandNumber.LIGHT.value,
    light_turn_on_command,
    light_turn_off_command
)
remote_controller.set_command(
    CommandNumber.TV.value,
    tv_turn_on_command,
    tv_turn_off_command
)
remote_controller.set_command(
    CommandNumber.GAME.value,
    game_turn_on_command,
    game_turn_off_command
)

remote_controller.turn_on_command(CommandNumber.LIGHT.value)
remote_controller.turn_off_command(CommandNumber.LIGHT.value)
remote_controller.turn_on_command(CommandNumber.TV.value)
remote_controller.turn_off_command(CommandNumber.TV.value)
remote_controller.undo_command()
remote_controller.turn_on_command(CommandNumber.GAME.value)
remote_controller.turn_off_command(CommandNumber.GAME.value)
