class TennisGame:
    SCORE = ["Love", "Fifteen", "Thirty", "Forty"]
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        elif player_name == self.player2_name:
            self.m_score2 += 1

    def get_score(self):
        if self.game_is_tied():
            return self.get_tied_score()
        elif self.game_is_endgame():
            return self.get_endgame_score()
        else:
            return self.get_regular_score()

    def get_tied_score(self):
        if self.m_score1 < len(self.SCORE):
            return f"{self.SCORE[self.m_score1]}-All"
        return "Deuce"


    def game_is_tied(self):
        return self.m_score1 == self.m_score2

    
    def game_is_endgame(self):
        return self.m_score1 >= 4 or self.m_score2 >= 4

    def get_endgame_score(self):
        score_difference = self.m_score1 - self.m_score2
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        elif score_difference <= -2:
            return f"Win for {self.player2_name}"

    def get_regular_score(self):
        player1_points = self.SCORE[self.m_score1]
        player2_points = self.SCORE[self.m_score2]
        return f"{player1_points}-{player2_points}"