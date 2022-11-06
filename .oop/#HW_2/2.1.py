"""
Перепишите класс, описывающий тетраэдр, таким образом, чтобы каждый атрибут был доступен только через геттеры,
а устанавливался только через сеттеры.
"""
import math


class Tetrahedron:
    """
    Класс, описывающий тетраэдр
    """
    def __init__(self, length=None):
        self._length = length

    @property
    def dimension(self):
        return f'Площадь тетраэдра со стороной {self._length} составляет {round(self._length ** 2 * math.sqrt(3),2)},' \
               f' а объем составляет {round(math.sqrt(2) / 12 * self._length ** 3, 2)}.'

    @dimension.setter
    def dimension(self, len_tet):
        self._length = len_tet


a = Tetrahedron()
a.dimension = 4
print(a.dimension)
