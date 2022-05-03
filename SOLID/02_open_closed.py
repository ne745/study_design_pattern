# open_closed.py
# 開放閉鎖の原則

from abc import ABCMeta, abstractmethod


class UserInfo:

    def __init__(self, user_name, job_name, nationality) -> None:
        self.user_name = user_name
        self.job_name = job_name
        self.nationality = nationality

    def __str__(self) -> str:
        return f"{self.user_name} {self.job_name} {self.nationality}"


# フィルターを追加する場合にクラス自体を編集する必要がある
# class UserInfoFilter:
#
#     @staticmethod
#     def filter_users_job(users, job_name):
#         for user in users:
#             if user.job_name == job_name:
#                 yield user
#
#     @staticmethod
#     def filter_users_nationality(users, nationality):
#         for user in users:
#             if user.nationality == nationality:
#                 yield user


class Comparation(metaclass=ABCMeta):

    @abstractmethod
    def is_equal(self, other):
        pass

    def __and__(self, other):
        return AndComparation(self, other)

    def __or__(self, other):
        return OrComparation(self, other)


class AndComparation(Comparation):

    def __init__(self, *args):
        self.comparations = args  # リスト

    def is_equal(self, other):
        # self.comparetions のすべての要素の is_equal メソッドを実行して
        # すべて　 True であれば True を返す
        return all(
            map(
                lambda comparation: comparation.is_equal(other),
                self.comparations
            )
        )


class OrComparation(Comparation):

    def __init__(self, *args):
        self.comparations = args  # リスト

    def is_equal(self, other):
        # self.comparetions のすべての要素の is_equal メソッドを実行して
        # いずれか　 True であれば True を返す
        return any(
            map(
                lambda comparation: comparation.is_equal(other),
                self.comparations
            )
        )


class Filter(metaclass=ABCMeta):

    @abstractmethod
    def filter(self, comparation, items):
        pass


class JobNameComparation(Comparation):

    def __init__(self, job_name) -> None:
        self.job_name = job_name

    def is_equal(self, other):
        return self.job_name == other.job_name


class NationalityComparation(Comparation):

    def __init__(self, nationality) -> None:
        self.nationality = nationality

    def is_equal(self, other):
        return self.nationality == other.nationality


class UserInfoFilter(Filter):

    def filter(self, comparation, items):
        for item in items:
            if comparation.is_equal(item):
                yield item


taro = UserInfo('taro', 'salary man', 'Japan')
jiro = UserInfo('jiro', 'police man', 'Japan')
john = UserInfo('jhon', 'salary man', 'USA')

user_list = [taro, jiro, john]

# for man in UserInfoFilter.filter_users_job(user_list, 'police man'):
#     print(man)

# for man in UserInfoFilter.filter_users_nationality(user_list, 'Japan'):
#     print(man)

user_info_filter = UserInfoFilter()

salary_man_comparation = JobNameComparation('salary man')
for user in user_info_filter.filter(salary_man_comparation, user_list):
    print(user)

japan_comparation = NationalityComparation('Japan')
for user in user_info_filter.filter(japan_comparation, user_list):
    print(user)

print('-' * 50)
salary_man__and_japan = salary_man_comparation & japan_comparation
for user in user_info_filter.filter(salary_man__and_japan, user_list):
    print(user)

print('-' * 50)
salary_man__and_japan = salary_man_comparation | japan_comparation
for user in user_info_filter.filter(salary_man__and_japan, user_list):
    print(user)
