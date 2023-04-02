import random

typing_dict = {
    "Normal":0,
    "Fighting":1,
    "Flying":2,
    "Poison":3,
    "Ground":4,
    "Rock":5,
    "Bug":6,
    "Ghost":7,
    "Steel":8,
    "Fire":9,
    "Water":10,
    "Grass":11,
    "Electric":12,
    "Psychic":13,
    "Ice":14,
    "Dragon":15,
    "Dark":16,
    "Fairy":17
}

# https://bulbapedia.bulbagarden.net/wiki/Type/Type_chart
type_chart = [[1.0 for _ in range(18)] for _ in range(18)]

type_chart[0][5] = 0.5
type_chart[0][7] = 0.0
type_chart[0][8] = 0.5

type_chart[1][0] = 2.0
type_chart[1][2] = 0.5
type_chart[1][3] = 0.5
type_chart[1][5] = 2.0
type_chart[1][6] = 0.5
type_chart[1][7] = 0.0
type_chart[1][8] = 2.0
type_chart[1][13] = 0.5
type_chart[1][16] = 2.0
type_chart[1][17] = 0.5

type_chart[2][1] = 2.0
type_chart[2][5] = 0.5
type_chart[2][6] = 2.0
type_chart[2][8] = 0.5
type_chart[2][11] = 2.0
type_chart[2][12] = 0.5

type_chart[3][3] = 0.5
type_chart[3][4] = 0.5
type_chart[3][5] = 0.5
type_chart[3][7] = 0.5
type_chart[3][8] = 0.0
type_chart[3][11] = 2.0
type_chart[3][17] = 2.0

type_chart[4][2] = 0.0
type_chart[4][3] = 2.0
type_chart[4][5] = 2.0
type_chart[4][6] = 0.5
type_chart[4][8] = 2.0
type_chart[4][9] = 2.0
type_chart[4][11] = 0.5
type_chart[4][12] = 2.0

type_chart[5][1] = 0.5
type_chart[5][2] = 2.0
type_chart[5][4] = 0.5
type_chart[5][6] = 2.0
type_chart[5][8] = 0.5
type_chart[5][9] = 2.0
type_chart[5][14] = 2.0

type_chart[6][1] = 0.5
type_chart[6][2] = 0.5
type_chart[6][3] = 0.5
type_chart[6][7] = 0.5
type_chart[6][8] = 0.5
type_chart[6][9] = 0.5
type_chart[6][11] = 2.0
type_chart[6][13] = 2.0
type_chart[6][16] = 2.0
type_chart[6][17] = 0.5

type_chart[7][0] = 0.0
type_chart[7][7] = 2.0
type_chart[7][13] = 2.0
type_chart[7][16] = 0.5

type_chart[8][5] = 2.0
type_chart[8][8] = 0.5
type_chart[8][9] = 0.5
type_chart[8][10] = 0.5
type_chart[8][12] = 0.5
type_chart[8][14] = 2.0
type_chart[8][17] = 2.0

type_chart[9][5] = 0.5
type_chart[9][6] = 2.0
type_chart[9][8] = 2.0
type_chart[9][9] = 0.5
type_chart[9][10] = 0.5
type_chart[9][11] = 2.0
type_chart[9][14] = 2.0
type_chart[9][15] = 0.5

type_chart[10][4] = 2.0
type_chart[10][5] = 2.0
type_chart[10][9] = 2.0
type_chart[10][10] = 0.5
type_chart[10][11] = 0.5
type_chart[10][15] = 0.5

type_chart[11][2] = 0.5
type_chart[11][3] = 0.5
type_chart[11][4] = 2.0
type_chart[11][5] = 2.0
type_chart[11][6] = 0.5
type_chart[11][8] = 0.5
type_chart[11][9] = 0.5
type_chart[11][10] = 2.0
type_chart[11][11] = 0.5
type_chart[11][15] = 0.5

type_chart[12][2] = 2.0
type_chart[12][4] = 0.0
type_chart[12][10] = 2.0
type_chart[12][11] = 0.5
type_chart[12][12] = 0.5
type_chart[12][15] = 0.5

type_chart[13][1] = 2.0
type_chart[13][3] = 2.0
type_chart[13][8] = 0.5
type_chart[13][13] = 0.5
type_chart[13][16] = 0.0

type_chart[14][2] = 2.0
type_chart[14][4] = 2.0
type_chart[14][8] = 0.5
type_chart[14][9] = 0.5
type_chart[14][10] = 0.5
type_chart[14][11] = 2.0
type_chart[14][14] = 0.5
type_chart[14][15] = 2.0

type_chart[15][8] = 0.5
type_chart[15][15] = 2.0
type_chart[15][17] = 0.0

type_chart[16][1] = 0.5
type_chart[16][7] = 2.0
type_chart[16][13] = 2.0
type_chart[16][16] = 0.5
type_chart[16][17] = 0.5

type_chart[17][1] = 2.0
type_chart[17][3] = 0.5
type_chart[17][8] = 0.5
type_chart[17][9] = 0.5
type_chart[17][15] = 2.0
type_chart[17][16] = 2.0

class Player:
    def __init__(self, name, typing):
        self.name = name
        self.info = typing
        if len(typing.split("/")) == 2:
            self.type1, self.type2 = typing.split("/")
        elif len(typing.split("/")) > 2:
            assert(false)
        else:
            self.type1 = typing
            self.type2 = ""

def play(player1, player2, best_of=9):
    description = ""
    p1score = 0
    p2score = 0
    p1prob = getProb(getEff(player1, player2))
    p2prob = getProb(getEff(player2, player1))
    description += f"[{p1prob*100}% vs {p2prob*100}%]: "
    not_done = True
    while(not_done):
        p1add, p2add = resolve(p1prob, p2prob)
        p1score += p1add
        p2score += p2add
        description += f"{p1score}-{p2score}, "
        if p1score > best_of/2.0 and p1score > p2score:
            winner = True
            not_done = False
        elif p2score > best_of/2.0 and p2score > p1score:
            winner = False
            not_done = False
    description = description[:len(description)-2] # Remove trailing comma and space
    score = f"{p1score}-{p2score}"
    return winner, score, description
    
def resolve(p, q):
    a = 1 if random.random() < p else 0
    b = 1 if random.random() < q else 0
    return a, b
    
def getProb(eff):
    return eff/2.0 if eff <= 1 else 0.5+((eff-1)/(2.0*eff))
    
def getEff(attacker, defender):
    p = 1.0
    q = 1.0
    
    p *= type_chart[typing_dict[attacker.type1]][typing_dict[defender.type1]]
    if defender.type2 != "":
        p *= type_chart[typing_dict[attacker.type1]][typing_dict[defender.type2]]
        
    if attacker.type2 == "":
        q = 0.0
    else:
        q *= type_chart[typing_dict[attacker.type2]][typing_dict[defender.type1]]
        if defender.type2 != "":
            q *= type_chart[typing_dict[attacker.type2]][typing_dict[defender.type2]]
            
    return p if p > q else q