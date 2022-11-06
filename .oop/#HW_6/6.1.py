"""
Продолжаем совершенствовать класс для работы с матрицами

Добавьте в класс Matrix несколько статических методов для быстрого создания определённых часто используемых матриц:
единичной, диагональных и т.п.

Такие методы принимают набор параметров, отличающийся от конструктора — чаще всего в сторону уменьшения,
либо большего удобства использования.
Далее в коде метода нужным способом создаётся новый экземпляр, при необходимости дополнительно настраиваются
его атрибуты.
В конце такой метод возвращает этот экземпляр.

Пример:


class Matrix:
    ...

@staticmethod
    def create_identity(...):
    '''Возвращает единичную матрицу заданной размерности.'''
        new = Matrix(...)
        ...
        return new


idm1 = Matrix.create_identity(...)
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

    @staticmethod
    def creating_single_matrix(n):
        """Возвращает единичную матрицу заданной размерности."""
        list_for_matrix = []
        for i in range(0, n):
            list_for_row = []
            for j in range(0, n):
                if i == j:
                    list_for_row.append(1)
                else:
                    list_for_row.append(0)
            list_for_matrix.append(list_for_row)

        new_matrix = Matrix(list_for_matrix)
        return new_matrix

    @staticmethod
    def creating_diagonal_matrix(list_m):
        """Возвращает диагональную матрицу."""
        n = len(list_m)
        list_for_matrix = []
        for i in range(0, n):
            list_for_row = []
            for j in range(0, n):
                if i == j:
                    list_for_row.append(list_m[j])
                else:
                    list_for_row.append(0)
            list_for_matrix.append(list_for_row)

        new_matrix = Matrix(list_for_matrix)
        return new_matrix

    @staticmethod
    def creating_zero_matrix(n):
        """Возвращает нулевую матрицу."""
        list_for_matrix = []
        for i in range(0, n):
            list_for_row = []
            for j in range(0, n):
                list_for_row.append(0)
            list_for_matrix.append(list_for_row)

        new_matrix = Matrix(list_for_matrix)
        return new_matrix


idm1 = Matrix.creating_single_matrix(3)
print('Единичная матрица:', idm1, sep="\n")
c = [1, 8, 15]
idm2 = Matrix.creating_diagonal_matrix(c)
print('Диагональная матрица:', idm2, sep="\n")
idm3 = Matrix.creating_zero_matrix(3)
print('Нулевая матрица:', idm3, sep="\n")
