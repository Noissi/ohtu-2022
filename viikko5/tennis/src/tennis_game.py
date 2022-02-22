class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.pisteTulosteet = ["Love", "Fifteen", "Thirty", "Forty"];

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.draw()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.forty()
        return self.points(self.m_score1) + "-" + self.points(self.m_score2)

    def draw(self):
        if self.m_score1 <= 3:
            return self.pisteTulosteet[self.m_score1] + "-All"
        return "Deuce"

    def forty(self):
        minus_result = self.m_score1 - self. m_score2
        if minus_result > 0:
            winning_player = self.player1_name
        else:
            winning_player = self.player2_name

        if abs(minus_result) == 1:
            return "Advantage " + winning_player
        return "Win for " + winning_player
    
    def points(self, m_score):
        return self.pisteTulosteet[m_score]
