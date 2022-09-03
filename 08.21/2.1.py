"""
Напишите декоратор для оценки времени выполнения функции.
Используйте модуль time, функции perf_counter и perf_counter_ns.
"""
# СДЕЛАТЬ: установите текстовый курсор на имя модуля, нажмите Alt+Enter и выберите действие Convert to 'from time import ...' — и так и оставьте; из большинства модулей и пакетов стандартной библиотеки мы импортируем с помощью from import
import time


# ИСПРАВИТЬ: аннотации и документация обязательны
def count_time_nanosecond(function):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter_ns()
        # ДОБАВИТЬ: а как же возвращаемое значение функции?
        function(*args, **kwargs)
        result = time.perf_counter_ns() - start_time
        print(f'Время выполнения {result} наносекунд')
    return wrapper


# ИСПРАВИТЬ: аннотации и документация обязательны
def count_time_second(function):
    def wrapper1(*args, **kwargs):
        start_time1 = time.perf_counter()
        # ДОБАВИТЬ: а как же возвращаемое значение функции?
        function(*args, **kwargs)
        time.sleep(1)
        result1 = time.perf_counter() - start_time1
        print(f'Время выполнения {result1} секунд')
    return wrapper1


@count_time_second
@count_time_nanosecond
def func(cel):
    for i in range(cel):
        return i


func(10)


"""
Время выполнения 6000 наносекунд
Время выполнения 1.003897800008417 секунд
"""

# ИТОГ: хорошо — 4/5
