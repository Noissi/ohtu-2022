class Player:
    def __init__(self, name, nationality, team, goals, assists, penalties, games):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists
        self.penalties = penalties
        self.games = games
        self.points = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20}" + f"{self.team:4}" + f"{str(self.goals):>2}" + ' + ' + f"{str(self.assists):>2}" + ' = ' + f"{str(self.points):>2}"
