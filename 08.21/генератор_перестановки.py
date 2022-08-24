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

set_per = {'a', 'b', 'c'}


def permutations(set_p):
    list_var = []
    perm_list = list(itertools.permutations(set_p))
    for elen_perm_list in perm_list:
        elem_list_var = ''
        if len(elen_perm_list) > 0:
            for i in range(0, len(elen_perm_list)):
                elem_list_var += elen_perm_list[i]
            list_var.append(elem_list_var)
    for j in range(0, len(list_var)):
        yield list_var[j]


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
