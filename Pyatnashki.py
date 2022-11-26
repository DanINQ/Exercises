import random
def play():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    sorted_numbers = numbers
    def shuflled_numbers():
        random.shuffle(numbers)
        pairs = 0
        for i in range(len(numbers)):
            for g in range(len(numbers)):
                if g > i:
                    if numbers[i] > numbers[g]:
                        pairs = pairs + 1
        pairs += 4
        return pairs
    while shuflled_numbers() % 2 != 0:
        shuflled_numbers()
    numbers.append([])
    empty = numbers.index([])
    print('Hello! Use keys W,A,S,D to change the position of empty place!\n\n')
    def visulalization():
        i = 0
        g = 1
        f = 2
        e = 3
        while i != 16:
            print(numbers[i], numbers[g], numbers[f], numbers[e])
            i += 4
            g += 4
            f += 4
            e += 4
    def w():
        if empty >= 4:
            w_var = empty-4
            numbers[empty], numbers[w_var] = numbers[w_var], numbers[empty]
        else:
            print("Can't move up!")
    def s():
        if empty <= 11:
            s_var = empty+4
            numbers[empty], numbers[s_var] = numbers[s_var], numbers[empty]
        else:
            print("Can't move down!")
    def a():
        if empty % 4 != 0:
            a_var = empty-1
            numbers[empty], numbers[a_var] = numbers[a_var], numbers[empty]
        else:
            print("Can't move left!")
    def d():
        if (empty+1) % 4 != 0:
            d_var = empty+1
            numbers[empty], numbers[d_var] = numbers[d_var], numbers[empty]
        else:
            print("Can't move right!")
    def control_def():
        if control in ['w','W','ц','Ц']:
            w()
        elif control in ['s','S','ы','Ы']:
            s()
        elif control in ['a','A','ф','Ф']:
            a()
        elif control in ['d','D','в','В']:
            d()
    while numbers == sorted_numbers:
        visulalization()
        control = (input('Enter key: '))
        if control in ['w', 'a', 's', 'd', 'W', 'A', 'S', 'D', 'ц', 'ф', 'ы', 'в', 'Ц', 'Ф', 'Ы', 'В']:
            print('\n\n')
            control_def()
            empty = numbers.index([])
        else:
             print('\nNope! WASD only!\n')
    print('Hey! Game Finished!')

play()