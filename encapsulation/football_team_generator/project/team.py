from typing import Union

from project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players: list[Player] = []
        self._test  = 5

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name) -> Union[Player, str]:
        try:
            player = [p for p in self.__players if p.name == player_name][0]
            self.__players.remove(player)
            return player
        except IndexError:
            return f"Player {player_name} not found"

    @property
    def all_players_count(self):
        return len(self.__players)