"""
Напишите класс, который описывает правильный тетраэдр по заданной в конструкторе длине ребра.
Добавьте методы, вычисляющие площадь поверхности и объём тетраэдра.
Продемонстрируйте на экземпляре.
"""
import math


class Tetrahedron:
    length: float

    def __init__(self, length: float):
        self.length = length

    # Рассчет площади:
    def square(self):
        return f'Площадь тетраэдра со стороной {self.length} составляет {round(self.length ** 2 * math.sqrt(3),2)}'

    # Рассчет объема:
    def volume(self):
        return f'Объем тетраэдра со стороной {self.length} составляет {round(math.sqrt(2) / 12 * self.length ** 3, 2)}'


a = Tetrahedron(5)
print(a.square())
print(a.volume())
