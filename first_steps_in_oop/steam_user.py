class SteamUser:

    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game_name, hours):
        if game_name not in self.games:
            return f"{game_name} is not in library"

        self.played_hours += hours
        return f"{self.username} is playing {game_name}"

    def buy_game(self, game_name):
        if game_name in self.games:
            return f"{game_name} is already in your library"

        self.games.append(game_name)
        return f"{self.username} bought {game_name}"

    def status(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"


user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())

