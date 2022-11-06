"""
Есть класс Алфавит, характеристиками которого являются:
  - язык
  - список букв

Для Алфавита можно:
  - напечатать все буквы алфавита
  - посчитать количество букв

Так же есть подклассы с русским и английским алфавитами, которые обладают следующими свойствами:
  - язык
  - список букв
  - количество букв

Для подклассов можно:
  - посчитать количество букв
  - определить, относится ли буква к алфавиту текущего подкласса
  - получить пример текста на соответствующем языке

Реализуйте эти возможности используя наследование и (до-)переопределение методов.
"""
import string


# класс Алфавит
class Alphabet:

    def __init__(self, language, letters_str):
        self.lang = language
        self.letters = list(letters_str)

    # Выводим все буквы алфавита
    def print(self):
        print(self.letters)

    # Считаем количество букв в алфавите
    def letters_num(self):
        len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    # Проверяем, относится ли буква к английскому алфавиту
    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False

    # Возвращаем количество букв в алфавите
    def letters_num(self):
        return EngAlphabet.__letters_num

    # Пример текста на английском языке
    @staticmethod
    def example():
        print("English Example: Fortune favors the bold.")


class RusAlphabet(Alphabet):
    __letters_num = 33

    def __init__(self):
        super().__init__('Rus', 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')

    # Проверяем, относится ли буква к русскому алфавиту
    def is_ru_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False

    # Выводим количество букв в алфавите
    def letters_num(self):
        return RusAlphabet.__letters_num

    # Пример текста на русском языке
    @staticmethod
    def example():
        print("Пример на русском языке: Победа любит подготовку.")


# Тесты
if __name__ == '__main__':
    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_en_letter('W'))
    print(eng_alphabet.is_en_letter('Ж'))
    EngAlphabet.example()

    rus_alphabet = RusAlphabet()
    rus_alphabet.print()
    print(rus_alphabet.letters_num())
    print(rus_alphabet.is_ru_letter('J'))
    print(rus_alphabet.is_ru_letter('Ф'))
    RusAlphabet.example()
