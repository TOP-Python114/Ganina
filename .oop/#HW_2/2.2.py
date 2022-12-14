"""
Реализуйте класс, в котором хранится информация об аутентификационных данных пользователя: логин и пароль.

Хранение пароля должно быть реализовано таким образом, чтобы строку с паролем нельзя было прочитать,
но можно было записать.
При этом для чтения должен быть доступен хэш пароля — для сравнения с хэшем вводимого очередной раз пароля.

Используйте геттер и сеттер для реализации этих требований.

Подсказка: в этой задаче используйте встроенную функцию hash() — однако,
она не является криптографически устойчивой, и для настоящих конфиденциальных данных её использовать нельзя.
"""


class User:
    """
    Класс, в котором хранится информация об аутентификационных данных пользователя: логин и пароль
    """

    def __init__(self, username: str, password: str):
        self.username = username
        self.__password = password

    @property
    def user_pas(self):
        return self.username, hash(self.__password)

    @user_pas.setter
    def user_pas(self, password):
        self.__password = password


a = User('Vasja', '00')
a.user_pas = '28K'
print(a.user_pas)
