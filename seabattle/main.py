from models import Player, Computer


def main():
    while True:
        mode = input('Enter the mode:\n'
                     '\n1 - with other player\n'
                     '2 - with computer\n')
        if mode == '1':
            players = [Player('Player1'), Player('Player2')]
            break
        elif mode == '2':
            while True:
                difficulty = input('\nChoose a difficulty:\n'
                                   '\n1 - Easy\n'
                                   '2 - Medium\n'
                                   '3 - Hard\n')
                if difficulty in ['1', '2', '3']:
                    break
            players = [Computer('Computer', difficulty), Player('Player1')]
            break

    for player in players:
        player.ship_perform()
        if type(player) != Computer:
            player.field.visualisation(player.field.ships_field)

    try:
        while True:
            for player in players:
                for attacked_player in players:
                    if attacked_player != player:
                        player.shot_perform(attacked_player)
                        attacked_player.field.visualisation(attacked_player.field.battle_field)
    except RuntimeError:
        print(player.name, ' won!')


main()
