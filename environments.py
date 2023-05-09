import numpy as np

class Machine():
    def __init__(self, name = None, payout = None):
        self.name = name
        assert payout is not None
        self.payout = payout
        
    def get_payout(self, d, b):
        return self.payout[d][b]
    
    def play(self, player):
        d = player.d
        b = player.b
        prob = self.get_payout(d,b)
        return 1 if np.random.random() < prob else 0

class Player():
    def __init__(self, prob_d = None, prob_b = None, name = 'Player',):
        self.name = name
        self.d = 1 if np.random.random() < prob_d else 0
        self.b = 1 if np.random.random() < prob_b else 0
    
    def __repr__(self):
        return f"{self.name},  d : {self.d}, b:{self.b}"