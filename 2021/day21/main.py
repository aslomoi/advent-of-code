p1_start = 8
p2_start = 3

class Die:
    face = 0
    rolls = 0

    def roll(self):
        self.rolls += 1
        self.face += 1
        if self.face > 100:
            self.face -= 100

    def turn(self):
        score = 0
        for _ in range(3):
            self.roll()
            score += self.face
        return score



class Player:
    def __init__(self, start):
        self.space = start
        self.score = 0
    def move(self, die):
        self.space += die.turn() % 10
        if self.space > 10:
            self.space = self.space % 10
        self.score += self.space

die = Die()
p1 = Player(p1_start)
p2 = Player(p2_start)

while True:
    p1.move(die)
    if p1.score >= 1000:
        break
    p2.move(die)
    if p2.score >= 1000:
        break

print(f"Part 1: {min(p1.score, p2.score) * die.rolls}")

from collections import Counter
from itertools import product

dirac = Counter((sum(x) for x in product([1,2,3],repeat=3)))

def quantum(p1, p2, w1, w2):

    # for num, freq in dirac.items():
    #     p1 = p1 +
    pass
