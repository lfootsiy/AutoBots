import random

class Player:
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice
        self.info = choice
        # Random per tournament
        if choice == '?':
            self.choice = random.choice(["R", "P", "S"])
        
    def getPlay(self):
        if self.choice != '??':
            return self.choice
        # Random per game
        else:
            return random.choice(["R", "P", "S"])
        
def play(player1, player2, **params):
    p1play = player1.getPlay()
    p2play = player2.getPlay()
    winner = resolve(p1play, p2play)
    description = f"{player1.name if winner else player2.name} won by playing {p1play if winner else p2play} against {p2play if winner else p1play}"
    score = "1-0" if winner else "0-1"
    return winner, score, description
    
def resolve(p1, p2):
    # Return true on p1 win
    # Return false on p2 win
    # TODO: make Enum with custom comparator to make this easier
    if p1 == p2:
        return random.choice([True, False])
    else:
        if p1 == 'R' and p2 == 'P':
            return False
        if p1 == 'R' and p2 == 'S':
            return True
        if p1 == 'P' and p2 == 'R':
            return True
        if p1 == 'P' and p2 == 'S':
            return False
        if p1 == 'S' and p2 == 'R':
            return False
        if p1 == 'S' and p2 == 'P':
            return True
        
    assert(false)