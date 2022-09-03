"""
В нейросетевых вычислениях широко испольузются перестановки некоторого множества элементов.
 Перестановки — это комбинации из n различных элементов, отличающиеся позициями элементов.
 Количество перестановок P = n!
 для 2 элементов a, b:
      ab ba
для 3 элементов a, b, c:
      abc bca cab acb cba bac

Напишите функцию-генератор, принимающую на вход множество set, и возвращающую в строковом
виде перестановки для элементов этого множества.
"""
import itertools


# ИСПРАВИТЬ: аннотации и документация обязательны
def permutations(set_p):
    # ИСПОЛЬЗОВАТЬ: не нужен ещё один список, если используете itertools.permutations()
    # list_var = []

    # ИСПРАВИТЬ: вот это никуда не годится — где строковые методы, где генераторные выражения?
    # perm_list = list(itertools.permutations(set_p))
    # for elen_perm_list in perm_list:
    #     elem_list_var = ''
    #     if len(elen_perm_list) > 0:
    #         for i in range(0, len(elen_perm_list)):
    #             elem_list_var += elen_perm_list[i]
    #         list_var.append(elem_list_var)
    # for j in range(0, len(list_var)):
    #     yield list_var[j]

    # ИСПОЛЬЗОВАТЬ:
    for perm in itertools.permutations(set_p):
        yield ''.join(str(elem) for elem in perm)


# ДОБАВИТЬ: за знание стандартной библиотеки хвалю, но предполагалось, что вы всё-таки напишите свой генератор перестановок


# СДЕЛАТЬ: для своей реализации добавьте во множество объект int и посмотрите, что получится
set_per = {'a', 'b', 'c'}
per = permutations(set_per)
for n in per:
    print(n)


"""
bca
bac
cba
cab
abc
acb
"""

# ИТОГ: можно лучше — 2/6
