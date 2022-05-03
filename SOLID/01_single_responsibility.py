# single_responsibility.py
# 単一責任の原則

class UserInfo:
    # ユーザ情報を保持する役割

    def __init__(self, name, age, phone_number) -> None:
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self) -> str:
        return f"{self.name}, {self.age}, {self.phone_number}"

    # ファイル情報を書き出す役割を持つため
    # 単一責任の原則に違反
    # def write_str_to_file(self, filename):
    #     with open(filename, mode='w') as f:
    #         f.write(str(self))


class FileManager:
    # ファイル操作をするクラスを追加

    @staticmethod
    def write_str_to_file(obj, filename):
        with open(filename, mode='w') as f:
            f.write(str(obj))


user_info = UserInfo('Taro', 21, '000-0000-0000')
print(user_info)
# user_info.write_str_to_file('temp.txt')
FileManager.write_str_to_file(user_info, 'temp.txt')
