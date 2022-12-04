from models import empty, damaged, missed, ship_point, Ship


def transform_input(input_coordinate):
    numbers = {
        '1': list(range(0, 10)),
        '2': list(range(10, 20)),
        '3': list(range(20, 30)),
        '4': list(range(30, 40)),
        '5': list(range(40, 50)),
        '6': list(range(50, 60)),
        '7': list(range(60, 70)),
        '8': list(range(70, 80)),
        '9': list(range(80, 90)),
        '10': list(range(90, 100)),
    }
    letters = {
        'А': list(range(0, 100, 10)),
        'Б': list(range(1, 101, 10)),
        'В': list(range(2, 102, 10)),
        'Г': list(range(3, 103, 10)),
        'Д': list(range(4, 104, 10)),
        'Е': list(range(5, 105, 10)),
        'Ж': list(range(6, 106, 10)),
        'З': list(range(7, 107, 10)),
        'И': list(range(8, 108, 10)),
        'К': list(range(9, 109, 10)),
    }
    coords = input_coordinate.split()
    if len(coords) == 2:
        if coords[0] in letters:
            if coords[1] in numbers:
                for i in letters[coords[0]]:
                    if i in numbers[coords[1]]:
                        return i


def ship_perform(player):
    def same_places_check(coordinates):
        for i in coordinates:
            if coordinates.count(i) > 1:
                raise IndexError

    def is_place_free(coordinates, player):
        for place in coordinates:
            for ship in player.field.ships:
                if place in ship.coordinates:
                    raise ValueError
        return True

    def ship_form(coordinates):
        matches = 0
        for i in coordinates:
            for g in coordinates:
                if i in list(range(0, 100, 10)):
                    if i - g == 1:
                        raise TypeError
                    elif i - g == -1:
                        matches -= 1
                    elif i - g == 10:
                        matches += 1
                elif i in list(range(9, 109, 10)):
                    if i - g == -1:
                        raise TypeError
                    elif i - g == 1:
                        matches -= 1
                    elif i - g == 10:
                        matches += 1
                elif i not in list(range(0, 100, 10)) + list(range(9, 109, 10)) and g not in list(
                        range(0, 100, 10)) + list(range(9, 109, 10)):
                    if i - g == 10:
                        matches += 1
                    elif i - g == 1:
                        matches -= 1

        if matches == len(coordinates) - 1:
            return True
        elif matches == -len(coordinates) + 1:
            return True
        raise TypeError

    def ships_nearby_check(coordinates, player):
        borders = {
            (0,): [-1, -10, -11],
            (9,): [1, -9, -10],
            (90,): [-1, 9, 10],
            (99,): [1, 10, 11],
            tuple(range(0, 100, 10)): [-10, -11, -1, 10, 9],
            tuple(range(9, 109, 10)): [10, 11, 1, -10, -9],
            tuple(range(0, 10)): [-9, -10, -11, -1, 1],
            tuple(range(90, 100)): [9, 10, 11, 1, -1]
        }

        for place in coordinates:
            matches = 0
            for border in borders:
                if place in border:
                    for i in borders[border]:
                        if player.field.ships_field[place - i] == ship_point:
                            raise KeyError
                    matches += 1
                    break
            if matches == 0:
                for i in [-1, -9, -10, -11, 1, 9, 10, 11]:
                    if player.field.ships_field[place - i] == ship_point:
                        raise KeyError

    while True:

        try:
            size = input(player.name + '\nEnter the ship size: \n')
            if size in player.field.ships_amount and player.field.ships_amount[size] != 0:
                coordinate_input = input(player.name +
                                         "\nEnter the ship coordinates dividing them by a comma ',',"
                                         " and each by a space ' '\n"
                                         "Like that 'Б 2,В 3,Г 9': \n")
                text_coordinates = coordinate_input.upper().split(',')
                coordinates = [transform_input(i) for i in text_coordinates]

                if len(coordinates) == int(size) and None not in coordinates:
                    same_places_check(coordinates)
                    is_place_free(coordinates, player)
                    ship_form(coordinates)
                    ships_nearby_check(coordinates, player)
                    ship = Ship(int(size))
                    player.field.ships.append(ship)
                    ship.coordinates = coordinates
                    for i in coordinates:
                        player.field.ships_field[i] = ship_point
                    player.field.ships_amount[size] -= 1
                    break
                else:
                    print('Not enough coordinates!\n')

        except ValueError as v:
            print('Oops! This place is already busy! \n', v)
        except IndexError as i:
            print('Do not enter same values please! \n', i)
        except TypeError as e:
            print("Nope! This ship can't be created! \n", e)
        except KeyError as k:
            print("Can't place ship here!", k)


def shot_perform(defense_player, player_name):
    while True:
        input_shot = input(player_name +
                           ' Enter the shot coordinate: ')
        shot = transform_input(input_shot.upper())

        if shot is not None:
            if defense_player.field.battle_field[shot] == empty:

                for ship in defense_player.field.ships:
                    if shot in ship.coordinates:
                        defense_player.field.battle_field[shot] = damaged
                        ship.damage += 1
                        if ship.damage == ship.size:
                            print('\nShip Destroyed!\n ')
                        else:
                            print('\nDamaged!\n')
                        return True
                defense_player.field.battle_field[shot] = missed
                print('\nNope! You missed!\n')
                return False

            else:
                print('Can not shoot here! ')
        else:
            print('Enter the correct coordinate! ')


def win_conditions(player):
    destroyed = 0
    for ship in player.field.ships:
        if ship.damage == ship.size:
            destroyed += 1
    if destroyed == len(player.field.ships):
        return True
