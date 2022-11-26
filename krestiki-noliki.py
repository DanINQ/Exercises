import random
def play():
    plane_list = ['[ ] ','[ ] ','[ ] ','[ ] ','[ ] ','[ ] ','[ ] ','[ ] ','[ ] ']
    game_figures = (' X  ', ' 0  ')
    player_figure = random.choice(game_figures)
    if player_figure == game_figures[0]:
        computer_figure = game_figures[1]
    else:
        computer_figure = game_figures[0]
    print('\nHello! Your playing figure is', player_figure)
    print('''\nUse numpad numbers accord to boxes of playing plane!
Or just use 1 - 9 keys. Like here:\n
              [7]  [8]  [9]\n
              [4]  [5]  [6]\n
              [1]  [2]  [3]\n
    ''')

    def visualisation():
        i = 8
        g = 7
        f = 6
        print('\n')
        while i != -1:
            print(plane_list[f], plane_list[g], plane_list[i],'\n')
            i -= 3
            g -= 3
            f -= 3


    def move():
        boolflag = False
        while boolflag == False:
            try:
                visualisation()
                user_move = input('Enter your move: ')
                int_user_move = int(user_move) - 1
                if plane_list[int_user_move] == '[ ] ':
                    plane_list[int_user_move] = player_figure
                    boolflag = True
                else:
                    print('\nSorry, this place is already busy!')
            except ValueError:
                print('\nUse numpad numbers only!')
            except IndexError:
                print('\nUse numpad numbers only!')


    def computer_move():
        boolflag = False
        for computer_move_var in range(len(plane_list)):
            if plane_list[computer_move_var] == '[ ] ':
                plane_list[computer_move_var] = player_figure
                if win_rules() == player_figure:
                    plane_list[computer_move_var] = '[ ] '
                    return computer_move_var
                plane_list[computer_move_var] = computer_figure
                if win_rules() == computer_figure:
                    return computer_move_var
                plane_list[computer_move_var] = '[ ] '
        while boolflag == False:
            computer_move_var = random.choice(range(len(plane_list)))
            if plane_list[computer_move_var] not in game_figures:
                boolflag = True
                return computer_move_var


    def win_rules():
        end_game_var = 1
        for i in game_figures:     #Проверяет победу по горизонтали
            for g in range(0,len(plane_list),3):
                if plane_list[g] == i:
                    if plane_list[g + 1] == i:
                        if plane_list[g + 2] == i:
                            end_game_var = i
            for g in range(0,3):    #Проверяет победу по вертикали
                if plane_list[g] == i:
                    if plane_list[g + 3] == i:
                        if plane_list[g + 6] == i:
                            end_game_var = i
            if plane_list[0] == i:                 #Проверяет победу по диагонали
                if plane_list[4] == i:
                    if plane_list[8] == i:
                        end_game_var = i
            if plane_list[2] == i:               #Проверяет победу по диагонали
                if plane_list[4] == i:
                    if plane_list[6] == i:
                        end_game_var = i

        if end_game_var == player_figure:
            return player_figure
        elif end_game_var == computer_figure:
            return computer_figure
        elif '[ ] ' not in plane_list:
            return 1

    def who_wins():
        if win_rules() == player_figure:
            print('\nCongrats! You are winner!')
            visualisation()
        elif win_rules() == computer_figure:
            print('\nOops! Seems like you loosed!')
            visualisation()
        elif win_rules() == 1:
            print('\nOops! Seems like nobody wins!')
            visualisation()

    while True:
        if player_figure == game_figures[0]:
            move()
            if win_rules() != None:
                who_wins()
                break
            plane_list[computer_move()] = computer_figure
            if win_rules() != None:
                who_wins()
                break
        else:
            plane_list[computer_move()] = computer_figure
            if win_rules() != None:
                who_wins()
                break
            move()
            if win_rules() != None:
                who_wins()
                break
play()