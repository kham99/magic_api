# Задание 1: Создание простого контекстного менеджера
# Напишите свой собственный контекстный менеджер, который будет открывать и закрывать файл для записи.
# Используйте ключевые слова __enter__ и __exit__.
# Пример:
# with FileWriter('example.txt') as file:
#     file.write("Hello, World!")
from contextlib import contextmanager
import time

class FileWriter:

    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileWriter("example.txt") as file:
    file.write("Hello, World!")



# Задание 2: Контекстный менеджер через contextlib
# Используйте библиотеку contextlib для создания контекстного менеджера, который будет отслеживать время выполнения
# блока кода.
#
# Пример:
# with time_tracker():
#     # Выполнение кода
#     time.sleep(1)


@contextmanager
def time_tracker():
    start_time = time.time()
    yield
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Функция {time_tracker.__name__} выполнена за {execution_time} секунд!")


with time_tracker():
    print("Тестирование времени выполнения кода!", 55 * 23)
    time.sleep(1)


# Задание 3: Обработка исключений
# Модифицируйте свой контекстный менеджер так, чтобы он корректно обрабатывал исключения,
# возникающие в блоке with. Попробуйте вывести тип ошибки, если она возникла.
#
# Пример:
# with ErrorHandlingContextManager():
#     raise ValueError("Something went wrong")


# @contextmanager
# def ErrorHandlingContextManager():
#     start_time = time.time()
#     error_occurred = False
#     try:
#         yield
#     except Exception as e:
#         error_occurred = True
#         print(f"Произошла ошибка: {type(e).__name__} - {e}")
#     finally:
#         end_time = time.time()
#         execution_time = end_time - start_time
#         if error_occurred:
#             print("Блок with завершился с ошибкой")
#         print(f"Время выполнения кода: {execution_time:.4f} секунд")
#
#
# with ErrorHandlingContextManager():
#     print("Тестирование времени выполнения кода!", 55 * 23)
#     time.sleep(1)
#     raise ValueError("Что-то пошло не так")



# Декораторы
#
# Задание 1: Декоратор для измерения времени выполнения функции
# Напишите декоратор, который измеряет и выводит время выполнения функции.
# Пример:
# @time_logger
# def example_function():
#      код


def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнена за {execution_time} секунд")
        return res
    return wrapper

@time_logger
def func_test():
    print("Test")
    time.sleep(1)
    print(55 * 123)


func_test()

