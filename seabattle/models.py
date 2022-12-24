import random
from tools import ship_checks, transform_input, shot_check, empty, damaged, missed, destroyed

# empty = ' '
# damaged = 'o'
# destroyed = 'X'
# missed = '*'
# ship_point = 'O'
ways = [1, 10]


class Field:
    def __init__(self):
        self.battle_field = [empty] * 100
        self.ships_field = [empty] * 100
        self.ships = []
        self.ships_amount = {
            '4': 1,
            '3': 2,
            '2': 3,
            '1': 4, }

    @staticmethod
    def visualisation(field):
        print("""
                 A   Б   В   Г   Д   Е   Ж   З   И   К
               |---|---|---|---|---|---|---|---|---|---|
            1  | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
               |---|---|---|---|---|---|---|---|---|---|
            2  | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
               |---|---|---|---|---|---|---|---|---|---|
            3  | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
               |---|---|---|---|---|---|---|---|---|---|
            4  | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
               |---|---|---|---|---|---|---|---|---|---|
            5  | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
               |---|---|---|---|---|---|---|---|---|---|
            6  | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
               |---|---|---|---|---|---|---|---|---|---|
            7  | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
               |---|---|---|---|---|---|---|---|---|---|
            8  | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
               |---|---|---|---|---|---|---|---|---|---|
            9  | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
               |---|---|---|---|---|---|---|---|---|---|
            10 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
               |---|---|---|---|---|---|---|---|---|---|
""".format(*field)
              )


class Player:
    def __init__(self, name):
        self.name = name
        # self.turn = turn
        self.field = Field()

    def ship_perform(self):
        while len(self.field.ships) != 10:
            self.field.visualisation(self.field.ships_field)
            while True:

                size = input(self.name + '\nEnter the ship size: \n')
                if size in self.field.ships_amount and self.field.ships_amount[size] != 0:
                    coordinate_input = input(self.name +
                                             "\nEnter the ship coordinates dividing them by a comma ',',"
                                             " and each by a space ' '\n"
                                             "Like that 'Б 2,В 3,Г 9': \n")
                    text_coordinates = coordinate_input.upper().split(',')
                    coordinates = [transform_input(i) for i in text_coordinates]

                    if len(coordinates) == int(size) and None not in coordinates:
                        try:
                            ship_checks(self, coordinates, size)
                            break
                        except ValueError as v:
                            print('Oops! This place is already busy! \n', v)
                        except IndexError as i:
                            print('Do not enter same values please! \n', i)
                        except TypeError as e:
                            print("Nope! This ship can't be created! \n", e)
                        except KeyError as k:
                            print("Can't place ship here!", k)
                    else:
                        print('Not enough coordinates!\n')

    def shot_perform(self, attacked_player):
        while True:
            attacked_player.field.visualisation(attacked_player.field.battle_field)
            input_shot = input(self.name +
                               ' Enter the shot coordinate: ')
            shot_var = transform_input(input_shot.upper())

            if shot_var is not None:
                result = shot_check(attacked_player, shot_var)
                if result == destroyed:
                    print('\nShip Destroyed!\n ')
                elif result == damaged:
                    print('\nDamaged!\n')
                elif result == missed:
                    print('\nNope! You missed!\n')
                    return None
                else:
                    print('Can not shoot here! ')

            else:
                print('\nEnter the correct coordinate! ')


# class Ship:
#     def __init__(self, size):
#         self.size = size
#         self.coordinates = []
#         self.damage = 0


class Computer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.aim = []

    def ship_perform(self):
        for size in self.field.ships_amount:
            while self.field.ships_amount[size] != 0:

                while True:
                    coordinates = [random.randint(0, 99)]
                    way = random.choice(ways)
                    while len(coordinates) != int(size):
                        new_coordinate = max(coordinates) + way
                        if new_coordinate >= 100:
                            new_coordinate = min(coordinates) - way
                        coordinates.append(new_coordinate)
                    try:
                        ship_checks(self, coordinates, size)
                        break
                    except Exception as e:
                        # print(e)
                        pass

    def shot_perform(self, attacked_player):
        print("\nComputer's turn.")
        shot_ways = [-1, 1, -10, 10]
        input('\nPress any key to continue\n')
        while True:
            if len(self.aim) == 0:
                shot_var = random.randint(0, 99)
                result = shot_check(attacked_player, shot_var)
                if result == damaged:
                    self.aim.append(shot_var)
                    print('Damaged!')
                    attacked_player.field.visualisation(attacked_player.field.battle_field)
                    input('\nPress any key to continue\n')
                elif result == destroyed:
                    self.aim = []
                    print('Destroyed!')
                    attacked_player.field.visualisation(attacked_player.field.battle_field)
                    input('\nPress any key to continue\n')
                elif result == missed:
                    print('Missed!')
                    return None
                # attacked_player.field.visualisation(attacked_player.field.battle_field)
            elif len(self.aim) > 1:
                # for i in self.aim:
                #     for g in self.aim:
                way = int(((self.aim[0] - self.aim[1]) ** 2) ** 0.5)
                shot_var = max(self.aim) + way

                while True:
                    if shot_var < 100:
                        result = shot_check(attacked_player, shot_var)
                        if result == damaged:
                            self.aim.append(shot_var)
                            print('Damaged!')
                            attacked_player.field.visualisation(attacked_player.field.battle_field)
                            input('\nPress any key to continue\n')
                            break
                        elif result == destroyed:
                            self.aim = []
                            print('Destroyed!')
                            attacked_player.field.visualisation(attacked_player.field.battle_field)
                            input('\nPress any key to continue\n')
                            break
                        elif result == missed:
                            print('Missed!')
                            return None
                        else:
                            shot_var = min(self.aim) - way

                    else:
                        shot_var = min(self.aim) - way

            elif len(self.aim) == 1:
                way = random.choice(shot_ways)
                shot_var = self.aim[0] + way
                if shot_var < 100:
                    result = shot_check(attacked_player, shot_var)
                    if result == damaged:
                        self.aim.append(shot_var)
                        print('Damaged!')
                        attacked_player.field.visualisation(attacked_player.field.battle_field)
                        input('\nPress any key to continue\n')
                    elif result == destroyed:
                        self.aim = []
                        print('Destroyed!')
                        attacked_player.field.visualisation(attacked_player.field.battle_field)
                        input('\nPress any key to continue\n')
                    elif result == missed:
                        print('Missed!')
                        return None
                    # attacked_player.field.visualisation(attacked_player.field.battle_field)

