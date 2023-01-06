import random


def gen():  # Нужно написать генератор, который бы каждый раз возвращал новое случайное значение
    while True:
        a = random.randint(0, 100)
        yield a


g = gen()

print(next(g))

print('\n\n\n')


def range_type_gen(start, end, step=1):  # Нужно написать генератор, который бы работал как range()
    num = start
    while num != end:
        num = num + step
        yield num


r = range_type_gen(0, 100, 5)

try:
    while True:
        print(next(r))
except StopIteration:
    print('Finished')

print('\n\n\n')


def map_type_gen(func, array):  # Нужно написать генератор, который бы работал как map()
    for i in array:
        yield func(i)


m = map_type_gen(lambda x: x * 3, [15, 56, 78, 56, 4, 672])

try:
    while True:
        print(next(m))
except StopIteration:
    print('Finished')

print('\n\n\n')


def enumerate_type_gen(array):  # Нужно написать генератор, который бы работал как enumerate()
    for i in array:
        yield i, array.index(i)


s = enumerate_type_gen([12, 234, 1, 32, 45, 91])

print('\n\n\n')


def zip_type_gen(array, array2):  # Нужно написать генератор, который бы работал как zip()
    for i in array:
        yield i, array2[array.index(i)]


z = zip_type_gen([12, 23, 12], ['first', 'second', 'third'])

try:
    while True:
        print(next(z))
except StopIteration:
    print('Finished')
