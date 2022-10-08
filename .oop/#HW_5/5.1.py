"""
Исключения

Придумайте и реализуйте с помощью наследования свою иерархию исключений для нужд класса Matrix.
Начните с того, в каких ситуациях вы бы хотели выбрасывать исключения при выполнении кода в классе Matrix.
Пример: попытка сложить матрицы разных размерностей.
Скопируйте код класса Matrix, над ним напишите свои классы исключений и используйте их в коде класса Matrix.
"""


class MatrixError(Exception):
    """Общий класс исключения для матриц"""
    pass


class MatrixSizeError(MatrixError):
    """
    Для обработки ошибок при сложении разноразмерных матриц
    """
    pass


class MatrixTypeError(MatrixError):
    """
    Для обработки ошибок при вычитании/сложении матрицы с числом
    """
    pass


class Matrix:
    """Класс матрицы"""
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:{len(self.my_list)}}", end=" ")
            print()
        return ''

    def __add__(self, other):
        """
        Поэлементное сложение:
        """
        if len(self.my_list) == len(other.my_list):
            for i in range(len(self.my_list)):
                for i_2 in range(len(other.my_list[i])):
                    self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
            return Matrix.__str__(self)
        else:
            raise MatrixSizeError

    def __sub__(self, other):
        """
        Поэлементное вычитание:
        """
        if type(self.my_list) == 'int' and type(other.my_list) == 'int':
            for i in range(len(self.my_list)):
                for i_2 in range(len(other.my_list[i])):
                    self.my_list[i][i_2] = self.my_list[i][i_2] - other.my_list[i][i_2]
            return Matrix.__str__(self)
        else:
            raise MatrixTypeError


m1 = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
m2 = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
m3 = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2]])

try:
    m6 = m1 + m3

except MatrixSizeError as exc:
    print('Матрицы должны быть одного размера!')
except MatrixTypeError as e:
    print('Действия производятся только над матрицами')
