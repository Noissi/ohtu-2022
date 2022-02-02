class PlayerStats:
    def __init__(self, reader):
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality):
        players = list(filter(lambda x: x.nationality == nationality, self.players))
        players.sort(key=lambda x: x.points, reverse=True)
        return players