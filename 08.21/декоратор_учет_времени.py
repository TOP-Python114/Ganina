"""
Напишите декоратор для оценки времени выполнения функции.
Используйте модуль time, функции perf_counter и perf_counter_ns.
"""

import time


def count_time_nanosecond(function):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter_ns()
        function(*args, **kwargs)
        result = time.perf_counter_ns() - start_time
        print(f'Время выполнения {result} наносекунд')
    return wrapper


def count_time_second(function):
    def wrapper1(*args, **kwargs):
        start_time1 = time.perf_counter()
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
