import time


# +1. Дан класс:
    # class Lock(object):
    #   def __init__(self):
    #     self.lock = False
    # 
    # Сделать менеджер контекста, который может переопределить 
    # значение lock на True внутри блока контекста.

class Lock(object):
    def __init__(self):
        self.lock = False

class Some:                                           # Я хз, вообще не понял че тут нужно сделать поменять атриббут обьекта или класса?
    def __init__(self, obj):                          # Атриббут класса здесь же не поменять т.к. self стоит
        self.obj = obj                      
    def __enter__(self):
        return self.obj
    def __exit__(self, *args):
        pass

g = Lock()


with Some(g) as l:
    l.lock = True

print(g.lock)



# +2. Сделать менеджер контекста, который бы проглатывал все исключения вызванные 
#    в теле и писал их в консоль, пример использования:
#     
#     with no_exceptions():
#       1 / 0 # => logs: ZeroDivisionError
# 
#     print('Done!') # => continues execution

class NoExceptions:
    def __init__(self):
        pass
    def __enter__(self):
        pass
    def __exit__(self, *args):
        print('log: ', args[0])
        return True

with NoExceptions():
    1/0
print('Done!')



# +3. Сделать менеджер контекста, который бы мог измерять время выполнения блока кода, 
#    пример использования:
#     
#     with TimeIt() as t:
#       some_long_function()
# 
#     print('Execution time was:', t.time)

class TimeIt:
    def __enter__(self):
        self.before = time.time()

    def __exit__(self, *args):
        self.after = time.time()
        print(self.after - self.before)

with TimeIt():
    time.sleep(2)