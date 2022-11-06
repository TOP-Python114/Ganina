"""
Перегрузка операторов
Реализовать класс для удобной работы с матрицами.

Класс должен поддерживать операции:
  - поэлементного сложения
  - поэлементного вычитания
  - поэлементного умножения на число
  - матричного умножения

Реализуйте для этого методы __add__ и __mul__. Вам также могут понадобиться вспомогательные методы.
Реализуйте метод __str__ для матрицы для форматированного вывода элементов матрицы.

Пример:

    class Matrix:
        ...

    m1 = Matrix(...)
    m2 = Matrix(...)

    m3 = m1 + m2
    m4 = 2 * m1

    print(m3)

    # stdout:
    #  2  3 10
    # 21 -5  7
    #  1  8 -4
    # -3 47  5

Придумайте несколько способов хранения элементов матрицы в атрибутах.
Реализуйте каждый из них, отмечая как меняется код методов в зависимости от используемой структуры хранения данных.
"""


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
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)

    def __sub__(self, other):
        """
        Поэлементное вычитание:
        """
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] - other.my_list[i][i_2]
        return Matrix.__str__(self)

    def __mul__(self, other):

        """
        Поэлементное умножение на число:
        """
        for i in range(len(self.my_list)):
            for i_2 in range(len(self.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] * other
        return Matrix.__str__(self)

    def __matmul__(self, other):
        """
        Матричное умножение:
        """
        res = [[0 for _ in range(len(self.my_list))] for _ in range(len(other.my_list))]

        for i in range(len(self.my_list)):
            for j in range(len(other.my_list[0])):
                for k in range(len(other.my_list)):
                    res[i][j] += self.my_list[i][k] * other.my_list[k][j]
        self.my_list = res

        return Matrix.__str__(self)


m1 = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
m2 = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])

# Поэлементное сложение:
m3 = m1 + m2
print(m3)

# Поэлементное вычитание:
m4 = m1 - m2
print(m4)

# Умножение на число:
num = 2
print(m1 * num)

# Умножение матриц
m5 = Matrix([[1, 2], [3, 4]])
m6 = Matrix([[5, 6], [7, 8]])
print(m5 @ m6)
