#1.Пользователь вводит число, если оно четное - выбрасываем исключение ValueError, если оно меньше 0 - TypeError, если оно больше 10 - IndexError. Обрабатываем ошибку, говорим пользователю, в чем его ошибка
def number_check(number):
    if number % 2 == 0:
        try:
            raise ValueError
        except ValueError:
            print('Oops! ValueError! Number is multiple by 2!')
    elif number < 0:
        try:
            raise TypeError
        except TypeError:
            print('Oops! TypeError! Number is less then zero!')
    elif number > 10:
        try:
            raise IndexError
        except IndexError:
            print('Oops! IndexError! Number is bigger then ten')
    else:
        print(number)


print('\n\n\n<<<Mowing next>>>\n\n\n')

#2. Создайте список произвольной длины. Пользователь должен ввести индекс объекта, который хочет посмотреть. Если все хорошо - пишите объект в консоль. Если нет - обработайте возмозможные ошибки и скажите ему, что не так
list1 = [12,24,567,1,'Hello!', False, 145, 'Smth', 'summat']

def list_obj_chooser():
    obj_number = input('Enter object number please.')
    try:
        print(list1[int(obj_number)])
    except ValueError:
        print('Oops! Looks like you entered not an integral!')



#1.Написать функцию, которая принимает на вход два аргумента. Если аргументы больше нуля, возвращаем их сумму. Если оба меньше - разность. Если знаки разные - возвращаем 0
def number_checker(arg1,arg2):
    if type(arg1) == int and type(arg2) == int:
        if arg1>0 and arg2 >0:
            return arg1 + arg2
        elif arg1 < 0 and arg2 < 0:
            return arg1 - arg2
        else:
            return 0
    else:
        raise ValueError('Oops! Wrong value!')



#2.Написать функцию, которая принимает 3 аргумента - числа, найти среди них два максимальных, вывести в консоль
def two_max_numbers(arg1,arg2,arg3):
    args_list = [arg1,arg2,arg3]
    min_arg = min(args_list)
    args_list.remove(min_arg)
    for i in args_list:
        print(i)



#3.Написать функцию, которая принимает два аргумента. Первый - список чисел, второй - булевый флаг. Если флаг действителен - возвращаем новый список с нечетными числами из входного списка, если флаг отрицателен - возвращаем новый список с четными числами из входного списка
def dunno_how_to_name_this(numbers, boolflag):
    sorted_numbers = []
    if bool(boolflag) == True:
        for i in numbers:
            if i % 2 != 0:
                sorted_numbers.append(i)
    else:
        for i in numbers:
            if i % 2 == 0:
                sorted_numbers.append(i)
    return(sorted_numbers)



#1.Написать функцию, которая принимает любое количество аргументов чисел. Среди них она находит максимальное и минимальное. И возвращает оба
def max_and_min(*numbers):
    max_and_min_var = max(numbers),min(numbers)
    return(max_and_min_var)



#2.Написать функцию, которая принимает два аргумента: строка и булевый флаг case по-умолчанию равный True. Если флаг действителен: возвращаем новую строку, где каждый символ входной приведен к верхнему регистру, иначе - к нижнему
def upper_lower_func(string, boolflag = True):
    if boolflag == True:
        return string.upper()
    else:
        return string.lower()


#3.Написать функцию, которая принимает любое количество позиционных аргументов - строк и один парматер по-умолчанию glue, который равен ':'. Соединить все строки таким образом, чтобы в результат попали все строки, длинее 3 символов. Для соединения между любых двух строк вставлять glue
def string_mixer(*strings, glue = ':'):
    big_string = ''
    for i in strings:
        if len(i) > 3:
            big_string += i
            big_string += glue
    return big_string