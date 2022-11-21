from time import time
import requests
from player import Player
from datetime import datetime

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
       
        player = Player(player_dict['name'], player_dict['team'], player_dict['nationality'], player_dict['goals'], player_dict['assists'])
        players.append(player)

    print("Players from FIN ", datetime.now(), "\n") 

    for player in players:
        print(player)

if __name__ == "__main__":
    main()