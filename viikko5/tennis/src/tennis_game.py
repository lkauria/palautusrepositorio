class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score1 = 0
        self.score2 = 0
        self.scores_str = "Love-All"

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.score1 += 1
        else:
            self.score2 += 1
        self.get_score()

    def get_score(self):
        if self.score1 == self.score2:
            if self.score1 < 3:
                self.scores_str = self.get_number_as_string(
                    self.score1) + "-All"
            else:
                self.scores_str = "Deuce"
        elif max(self.score1, self.score2) > 3 and abs(self.score1-self.score2) == 1:
            self.scores_str = "Advantage " + self.get_winning_player()
        elif max(self.score1, self.score2) < 4:
            self.scores_str = self.get_number_as_string(
                self.score1) + "-" + self.get_number_as_string(self.score2)
        else:
            self.scores_str = "Win for " + self.get_winning_player()
        return self.scores_str

    def get_number_as_string(self, balls):
        if balls == 0:
            return "Love"
        elif balls == 1:
            return "Fifteen"
        elif balls == 2:
            return "Thirty"
        else:
            return "Forty"

    def get_winning_player(self):
        if self.score1 > self.score2:
            return self.player1_name
        else:
            return self.player2_name
