"""
Напишите декоратор, который логирует вызов функции в файл-журнал, используя атрибуты объекта функции __name__
и аргументы, переданные функции.
***Примените его к функции checkhand() в файле poker.py
***Установите в цикле ожидание комбинации стрит и запустите скрипт.
***Делаю
Прикрепите файл-журнал вместе с файлом ответа.
"""
import logging


def logge_fun(func):

    def wrapper(*args, **kwargs):
        func_name = func.__name__
        log = logging.getLogger(func_name)
        log.setLevel(logging.INFO)

        fh = logging.FileHandler("%s.log" % func_name)
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        log.addHandler(fh)

        log.info("Start function: %s" % func_name)
        result = func(*args, **kwargs)
        log.info("Result function: %s" % result)
        return func

    return wrapper


@logge_fun
def multiple_number(a):
    b = a * 3
    return b


if __name__ == "__main__":
    value = multiple_number(5)
