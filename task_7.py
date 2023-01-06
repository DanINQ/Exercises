import time
from functools import reduce


def cancell_decorator(
        func):  # + Написать декоратор, который отменяет выполнение любой декорированной функций и будет писать в консоль: ИМЯ_ФУНКЦИИ is canceled!
    def inner(a):
        try:
            raise ValueError
        except ValueError as v:
            print(func.__name__, ' is cancelled!')

    return inner


@cancell_decorator
def some_func(a):
    print(a * 2)


# some_func(7)


print('\n\n\n')


def execution_time_log(func):  # + Реализовать декоратор, который измеряет скорость выполнения функций.
    def inner(a, b):
        before = time.time()
        func(a, b)
        after = time.time()
        execute_time = after - before
        print('Execution time is: ', execute_time)

    return inner


@execution_time_log
def some_func(a, b):
    s = list(range(1, 100))
    d = [i + a * b for i in s]
    sd = [i * a for i in s for a in d]
    print('Result is: ', d, ' seconds')


# some_func(25, 200)


print('\n\n\n')


def amount_of_repeats(func):  # + Реализовать декоратор, который будет считать, сколько раз выполнялась функция
    def inner(multiplier, number):
        a = 0
        repeats = 0
        while a < 1000:
            a += func(multiplier, number)
            repeats += 1
        print('Number of repeats: ', repeats)

    return inner


@amount_of_repeats
def some_func(multiplier, number):
    return number * multiplier


# some_func(5, 50)


print('\n\n\n')


def logging_decorator(
        func):  # + Реализовать декоторатор, который будет логгировать процесс выполнения функции: создан декоратор, начато выполнение функции, закончено выполнение функции
    # print('Decorator initialized!')           # uncomment me to work
    def inner(number):
        print('Function execution started!')
        result = func(number)
        print('Result is: ', result)
        print('Function execution finished!')

    return inner


@logging_decorator
def some_func(number):
    return number * number


# some_func(45)


print('\n\n\n')


def exception_catch(
        func):  # + Реализовать декоратор, который будет перехватывать все исключения в функции. Если они случились, нужно просто писать в консоль сообщение об ошибке
    def inner(*numbers):
        try:
            print(func(numbers))
        except Exception as e:
            print('Something went wrong! ', e)

    return inner


@exception_catch
def some_func(numbers):
    mapped = map(lambda x: x * x + (x % 2), numbers)
    return list(mapped)


# some_func(12,234,673,23,2,65,34)
# some_func(12, 'something')


a = map(lambda x: x % 5,
        [1, 4, 5, 30, 99])  # + При помощи map посчитать остаток от деление на 5 для чисел: [1, 4, 5, 30, 99]
print(list(a))

b = map(lambda x: str(x), [3, 4, 90, -2])  # + При помощи map превратить все числа из массива [3, 4, 90, -2] в строки
print(list(b))

c = filter(lambda x: type(x) != str, ['some', 1, 'v', 40, '3a',
                                      str])  # + При помощи filter убрать из массива ['some', 1, 'v', 40, '3a', str] все строки
print(list(c))


# d = reduce(lambda x, y: len(x) + len(y) if type(x) == str else x + len(y), ['some', 'other', 'value'])
def len_calc(x, y):
    if type(x) == str:
        return len(x) + len(y)
    else:
        return x + len(y)


d = reduce(len_calc, ['some', 'other',
                      'value'])  # + При помощи reduce посчитать количество букв в словах: ['some', 'other', 'value']
print(d)
