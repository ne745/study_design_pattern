# interpreter.py
from abc import ABC, abstractmethod


class InterpreterException(Exception):
    pass


# Context
# AbstractExpression によって構文解析されるクラス
class Context:

    def __init__(self, text) -> None:
        # 1 3 * -> [1, 3, *]
        self.__tokens = text.split()
        self.__idx = 0

    @property
    def tokens(self):
        pass

    @tokens.getter
    def tokens(self):
        return self.__tokens

    @property
    def idx(self):
        pass

    @idx.getter
    def idx(self):
        return self.__idx

    @idx.setter
    def idx(self, idx):
        self.__idx = idx

    def delete_token(self, start, end):
        del self.__tokens[start: end]


# AbstractExpression
# 構文木の各ノードに共通の処理を記載したインターフェース
class Node(ABC):

    @abstractmethod
    def parse(self, context: Context):
        pass


# NonTeminalExpression
# AbstractExpression を具体化したクラス
# 木構造の枝を表す
class ProgramNode(Node):

    def parse(self, context: Context):
        try:
            while context.idx < len(context.tokens):
                idx = context.idx
                current_token = context.tokens[idx]
                if current_token == '+':
                    node = PlusNode()
                elif current_token == '-':
                    node = MinusNode()
                elif current_token == '*':
                    node = MultiplyNode()
                elif current_token == '/':
                    node = DevideNode()
                else:
                    context.idx += 1
                    continue
                answer = node.parse(context)
                context.delete_token(idx - 2, idx + 1)
                context.tokens.insert(idx - 2, answer)
                context.idx = idx - 1
            if len(context.tokens) == 1:
                return context.tokens[0]
            else:
                raise InterpreterException('Expression is invalid.')
        except Exception:
            raise InterpreterException('Expression is invalid.')


# TerminalExpression
# AbstractExpression を具体化したクラス
# 木構造の葉を表す
class PlusNode(Node):

    def parse(self, context: Context):
        idx = context.idx
        return int(context.tokens[idx - 2]) + int(context.tokens[idx - 1])


# TerminalExpression
class MinusNode(Node):

    def parse(self, context: Context):
        idx = context.idx
        return int(context.tokens[idx - 2]) - int(context.tokens[idx - 1])


# TerminalExpression
class MultiplyNode(Node):

    def parse(self, context: Context):
        idx = context.idx
        return int(context.tokens[idx - 2]) * int(context.tokens[idx - 1])


# TerminalExpression
class DevideNode(Node):

    def parse(self, context: Context):
        idx = context.idx
        return int(context.tokens[idx - 2]) // int(context.tokens[idx - 1])


context = Context('2 1 --')
node = ProgramNode()
print(node.parse(context))
