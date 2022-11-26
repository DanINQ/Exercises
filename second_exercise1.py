main_list = [1,14,3,45,6,17,35,23,41]

main_list.sort()
print('Неотсортированный список чисел: ' + str(main_list))
print('Отсортировнный список чисел:' + str(main_list))

print('\n\n\n<<<Mowing next>>>\n\n\n')

dictionary1 = {15: '3*5', 121: '11**2', 545: '145 + 400',
               116: 'length of Hundred years war',
               6: "number of Michael Jordan's champion rings",
               18: "number of years of Putin's presidency"
               }

for i in dictionary1:
    print('| Ключ | Значение |')
    print(i,dictionary1[i])

print('\n\n\n<<<Mowing next>>>\n\n\n')

tuple1 = (3.14, 50.05, 134.000001, 0.33333334, 676.8989)

print('Кортеж tuple1:' + str(tuple1))

biggest_float = max(tuple1)
smallest_float = min(tuple1)

print('Максимальное значение кортежа tuple1: '+ str(biggest_float))
print('Минимальное значение кортежа tuple1: '+ str(smallest_float))


print('\n\n\n<<<Mowing next>>>\n\n\n')


geo_list = ['Moscow' , 'Earth' , 'Russia']

print(geo_list[1] + '->' + geo_list[2] + '->' + geo_list[0])


print('\n\n\n<<<Mowing next>>>\n\n\n')



exercise_str = '/bin:/usr/bin:/usr/local/bin'
splited_str = exercise_str.split(':')
print('Initial sting: ' + str(exercise_str))
print('Listed string: ' + str(splited_str))


print('\n\n\n<<<Mowing next>>>\n\n\n')

multiple_by_seven = []
not_multiple_by_seven = []
for i in range(1,100):
    if i % 7 == 0:
        multiple_by_seven.append(i)
    else:
        not_multiple_by_seven.append(i)

print('Numbers in range 1 to 100, multiple by 7: ')
print(multiple_by_seven)
print('Numbers in range 1 to 100, not multiple by 7: ')
print(not_multiple_by_seven)


print('\n\n\n<<<Mowing next>>>\n\n\n')


matrix_4X3 = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]]
print('Matrix:')
for i in matrix_4X3:
    print(i)

print('Matrix rows:')
for i in matrix_4X3:
    print(i[0], i[1], i[2])

print('Matrix columns:')
for i in matrix_4X3:
    print(i[0])
for i in matrix_4X3:
    print(i[1])
for i in matrix_4X3:
    print(i[2])


print('\n\n\n<<<Mowing next>>>\n\n\n')


new_list = ['something', "something else", 'Wachudoin',15, False]
for i in new_list:
    print('List value: ' + str(i))
    print('Value index: ' + str(new_list.index(i)))


print('\n\n\n<<<Mowing next>>>\n\n\n')


new_list2 = ['abc', 'to-delete', 'something', 'to-delete', None, 15469, 'to-delete']
print('List, needed to be cleaned: ' + str(new_list2))
for i in new_list2:
    if i == 'to-delete':
        new_list2.remove(i)

print('Cleaned list: ' + str(new_list2))


print('\n\n\n<<<Mowing next>>>\n\n\n')


finish_list = list(range(1,11))
finish_list.reverse()
for i in finish_list:
    print(i)