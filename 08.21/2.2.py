"""
Напишите декоратор, который логирует вызов функции в файл-журнал, используя атрибуты объекта функции __name__
и аргументы, переданные функции.
***Примените его к функции checkhand() в файле poker.py
***Установите в цикле ожидание комбинации стрит и запустите скрипт.
***Делаю
Прикрепите файл-журнал вместе с файлом ответа.
"""
# КОММЕНТАРИЙ: прям порадовался за такое знание стандартной библиотеки, молодец!
import logging


def logge_fun(func):

    def wrapper(*args, **kwargs):
        func_name = func.__name__
        log = logging.getLogger(func_name)
        log.setLevel(logging.INFO)

        # ИСПРАВИТЬ: этот способ форматирования строк устарел лет восемь-девять назад — так что закопайте его обратно, откуда выкопали и счастливо используйте f-строки, например здесь f'{func_name}.log'
        fh = logging.FileHandler("%s.log" % func_name)

        # КОММЕНТАРИЙ: к Formatter это не относится, там свой парсер
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        log.addHandler(fh)

        # ИСПРАВИТЬ: и землёй присыпьте хорошенько, когда закапывать будете
        log.info("Start function: %s" % func_name)
        result = func(*args, **kwargs)
        log.info("Result function: %s" % result)

        # ИСПРАВИТЬ: опечатка или ... ?
        return func

    return wrapper


@logge_fun
def multiple_number(a):
    b = a * 3
    return b


if __name__ == "__main__":
    value = multiple_number(5)

# ИТОГ: очень хорошо — 6/7
