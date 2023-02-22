#Just summing
def sum_all(*numbers):
    actually_sum = 0
    for i in numbers:
        actually_sum += i
    return actually_sum


#Random errors
import random
errors = (ValueError, TypeError, RuntimeError)
def random_error(errors):
    try:
        raise random.choice(errors)
    except ValueError as val_err:
        print('Wrong value!',val_err)
        return val_err
    except TypeError as type_err:
        print('Invalid Type!',type_err)
        return type_err
    except RuntimeError as rntm_err:
        print('Wha',rntm_err)
        return rntm_err


##Sorting tuple
#def int_tuple(values):
        #or i in values:
            #if not isinstance(i,int):
                    #raise ValueError('Oops!')
        #values.sort()
        #return(values)

#Sorting tuple
def int_tuple(values):
    gg = 0
    try:
        values.sort()
    except TypeError as e:
        print('Oooooops!')
        gg = e
    try:
        if gg != 0:
            raise ValueError
        else:
            print(values)
    except ValueError as v:
        print('Lools like some wrong value in here!', 'ValueError!!!')
#Mutating dictionary keys
def keys_mutating(dict):
    dict2={}
    for i in dict:
        dict2.update({str(i):dict[i]})
    return dict2

#Just multiplication of numbers

def sum_all(*numbers):
    actually_sum = 1
    for i in numbers:
        actually_sum *= i
    return actually_sum
