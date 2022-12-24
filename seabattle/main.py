from models import Player, Computer

from tools import win_conditions


def main():
    while True:
        mode = input('Enter the mode:\n'
                     '1 - with other player\n'
                     '2 - with computer\n')
        if mode == '1':
            players = [Player('Player1'), Player('Player2')]
            break
        elif mode == '2':
            players = [Computer('Computer'), Player('Player1')]
            break

    # for player in players:
    #
    #     while len(player.field.ships) != 10:
    #         player.field.visualisation(player.field.ships_field)
    #         ship_perform(player)

    # while True:
    #     for player in players:
    #         for def_player in players:
    #             if def_player != player:
    #                 def_player.field.visualisation(def_player.field.battle_field)
    #                 while shot_perform(def_player, player.name):
    #                     def_player.field.visualisation(def_player.field.battle_field)
    #                     if win_conditions(def_player):
    #                         print(player.name, ' won!')
    #                         return None

    for player in players:
        player.ship_perform()
        if type(player) != Computer:
            player.field.visualisation(player.field.ships_field)

    while True:
        for player in players:
            for attacked_player in players:

                if attacked_player != player:
                    player.shot_perform(attacked_player)
                    attacked_player.field.visualisation(attacked_player.field.battle_field)
                    if win_conditions(attacked_player):
                        print(player.name, ' won!')
                        return None
    # Try:
        # win_conditions
    # except


main()
