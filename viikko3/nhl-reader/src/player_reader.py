import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = []
        
        self.readPlayers()

    def readPlayers(self):
        response = requests.get(self.url).json()
        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists'],
                player_dict['penalties'],
                player_dict['games']
            )
    
            self.players.append(player)