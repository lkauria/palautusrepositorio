from player_reader import PlayerReader

class PlayerStats:

    def __init__(self, PlayerReader):

        self.players = PlayerReader.get_players()
        self.players.sort(key = lambda x: x.__scores__(), reverse = True)


    def top_players(self, country):
        
        players = []
        
        for player in self.players:
            if player.nationality == country:
                players.append(player)
        return players