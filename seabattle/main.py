from models import Field, Player, Ship
from models import empty, damaged, missed, ship_point
from tools import transform_input, ship_perform, shot_perform, win_conditions


def main():
    players = [Player('player1'), Player('player2')]

    for player in players:

        while len(player.field.ships) != 10:
            player.field.visualisation(player.field.ships_field)
            ship_perform(player)


    while True:
        for player in players:
            for def_player in players:
                if def_player != player:
                    def_player.field.visualisation(def_player.field.battle_field)
                    while shot_perform(def_player, player.name):
                        def_player.field.visualisation(def_player.field.battle_field)
                        if win_conditions(def_player):
                            print(player.name, ' won!')
                            return None



main()