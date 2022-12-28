empty = ' '
damaged = 'o'
destroyed = 'X'
missed = '*'
ship_point = 'O'


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


def ships_nearby_check(coordinates, field, point):
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
                    if field[place - i] == point:
                        raise KeyError
                matches += 1
                break
        if matches == 0:
            for i in [-1, -9, -10, -11, 1, 9, 10, 11]:
                if field[place - i] == point:
                    raise KeyError


def ship_checks(player, coordinates, size):
    same_places_check(coordinates)
    is_place_free(coordinates, player)
    ship_form(coordinates)
    ships_nearby_check(coordinates, player.field.ships_field, ship_point)
    ship = player.ship(int(size))
    player.field.ships.append(ship)
    ship.coordinates = coordinates
    for i in coordinates:
        player.field.ships_field[i] = ship_point
    player.field.ships_amount[size] -= 1


def shot_check(attacked_player, shot):
    if attacked_player.field.battle_field[shot] == empty:

        for ship in attacked_player.field.ships:
            if shot in ship.coordinates:
                attacked_player.field.battle_field[shot] = damaged
                ship.damage += 1
                if ship.damage == ship.size:
                    for i in ship.coordinates:
                        attacked_player.field.battle_field[i] = destroyed
                    return destroyed
                else:
                    return damaged
        attacked_player.field.battle_field[shot] = missed
        return missed

    else:
        return None


def win_conditions(player):
    destroyed_ships = 0
    for ship in player.field.ships:
        if ship.damage == ship.size:
            destroyed_ships += 1
            for i in ship.coordinates:
                player.field.battle_field[i] = destroyed
    if destroyed_ships == len(player.field.ships):
        raise RuntimeError
