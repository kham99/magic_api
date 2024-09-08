def sum_all(*args):
    count = 0
    for number in args:
        count += number
    return count, len(args)


print(sum_all(2, 6, 33, 66, 99))


def greet(**kwargs):
    for k, v in kwargs.items():
        if k == "name":
            print(f"Hello, {v}!")
        else:
            print("Hello!")


greet(name="John", age=25, city="New-York")


def process_data(*args, **kwargs):
    print(f"Количество позиционных аргументов: {len(args)}")
    print(f"Количество ключей в именованных аргументах: {len(kwargs)}")


process_data(3, 3, 5, 5, name="Amir", city="Moscow")


def process_data_sum(*args, **kwargs):
    count = 0
    for num in args:
        if isinstance(num, (float, int)):
            count += num
    for value in kwargs.values():
        if isinstance(value, (float, int)):
            count += value
    return count


print(process_data_sum(1, 3, 21, {3, 4, 5}, "fad", a=2, b=7, c="sdf", d=[2, 3, 4], e=9))





class Rectangle:
    rectangle1 = 1.1
    rectangle2 = 2.2
    rectangle3 = 2.2

