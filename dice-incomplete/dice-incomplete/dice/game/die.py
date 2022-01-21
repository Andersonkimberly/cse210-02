import random

class Die:

    def __init__(self):
        self.value = 0
        self.points = 0

    def roll(self):
        self.value = random.randint(1,6)
        if self.value == 1:
            self.points += 500
        elif self.value == 5:
            self.points += 50            
