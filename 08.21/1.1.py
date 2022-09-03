"""
Напишите итератор колоды карт (52 карты). При вызове функции next() будет представлена следующая карта.
Каждая карта представлена в виде кортежа типа (2, 'пики').
Номиналы: 1 — туз, 11 — валет, 12 — дама, 13 — король
Порядок следования мастей: черви, бубны, пики, крести.
"""
from random import choice


card_list = []
numbers_iterator = iter(card_list)
for i in ['черви', 'бубны', 'пики', 'крести']:
    for j in range(1, 14):
        card_list.append((j, i))
for _ in card_list:
    print(next(numbers_iterator))

# Реализуйте функцию-генератор для получения перемешанной колоды.
# Подсказка: используйте функцию choice() из модуля random


def mix_card(cards):
    card_list_mix = []
    while len(card_list_mix) < 52:
        card_mix = choice(cards)
        if card_mix not in card_list_mix:
            card_list_mix.append(card_mix)
            yield card_mix


print("\nПеремешанная колода карт:")
deck_mix_card = mix_card(card_list)
for i in deck_mix_card:
    print(i)

"""
(1, 'черви')
(2, 'черви')
(3, 'черви')
(4, 'черви')
(5, 'черви')
(6, 'черви')
(7, 'черви')
(8, 'черви')
(9, 'черви')
(10, 'черви')
(11, 'черви')
(12, 'черви')
(13, 'черви')
(1, 'бубны')
(2, 'бубны')
(3, 'бубны')
(4, 'бубны')
(5, 'бубны')
(6, 'бубны')
(7, 'бубны')
(8, 'бубны')
(9, 'бубны')
(10, 'бубны')
(11, 'бубны')
(12, 'бубны')
(13, 'бубны')
(1, 'пики')
(2, 'пики')
(3, 'пики')
(4, 'пики')
(5, 'пики')
(6, 'пики')
(7, 'пики')
(8, 'пики')
(9, 'пики')
(10, 'пики')
(11, 'пики')
(12, 'пики')
(13, 'пики')
(1, 'крести')
(2, 'крести')
(3, 'крести')
(4, 'крести')
(5, 'крести')
(6, 'крести')
(7, 'крести')
(8, 'крести')
(9, 'крести')
(10, 'крести')
(11, 'крести')
(12, 'крести')
(13, 'крести')

Перемешанная колода карт:
(7, 'бубны')
(1, 'черви')
(13, 'черви')
(1, 'пики')
(11, 'бубны')
(1, 'крести')
(12, 'черви')
(8, 'бубны')
(10, 'пики')
(12, 'крести')
(3, 'пики')
(13, 'крести')
(13, 'бубны')
(6, 'черви')
(10, 'крести')
(5, 'пики')
(1, 'бубны')
(8, 'пики')
(7, 'крести')
(5, 'черви')
(6, 'крести')
(13, 'пики')
(12, 'бубны')
(9, 'крести')
(3, 'крести')
(10, 'бубны')
(8, 'крести')
(7, 'черви')
(8, 'черви')
(2, 'черви')
(5, 'бубны')
(2, 'бубны')
(3, 'бубны')
(7, 'пики')
(6, 'бубны')
(12, 'пики')
(2, 'крести')
(11, 'черви')
(10, 'черви')
(11, 'пики')
(9, 'черви')
(4, 'бубны')
(4, 'черви')
(4, 'пики')
(9, 'пики')
(11, 'крести')
(6, 'пики')
(9, 'бубны')
(4, 'крести')
(3, 'черви')
(2, 'пики')
(5, 'крести')
"""