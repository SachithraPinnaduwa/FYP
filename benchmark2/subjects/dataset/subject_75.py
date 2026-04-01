import math

class EloRatingSystem:
    def __init__(self, k_factor: float = 32.0):
        self.k_factor = k_factor
        self.ratings = {}

    def add_player(self, player_id: str, initial_rating: float = 1200.0):
        if player_id not in self.ratings:
            self.ratings[player_id] = initial_rating

    def get_expected_score(self, rating_a: float, rating_b: float) -> float:
        return 1.0 / (1.0 + math.pow(10.0, (rating_b - rating_a) / 400.0))

    def record_match(self, player_a: str, player_b: str, score_a: float):
        # score_a: 1.0 for win, 0.5 for draw, 0.0 for loss
        if player_a not in self.ratings or player_b not in self.ratings:
            raise ValueError("Both players must be registered")

        r_a = self.ratings[player_a]
        r_b = self.ratings[player_b]

        expected_a = self.get_expected_score(r_a, r_b)
        expected_b = self.get_expected_score(r_b, r_a)

        score_b = 1.0 - score_a

        self.ratings[player_a] = r_a + self.k_factor * (score_a - expected_a)
        self.ratings[player_b] = r_b + self.k_factor * (score_b - expected_b)