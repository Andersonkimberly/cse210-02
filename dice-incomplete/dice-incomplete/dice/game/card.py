import random

class Card:

    def __init__(self):
        self.value = random.randint(1,13)
        self.value2 = 0
        self.points = 300
        

    def draw(self):
        self.value2 = random.randint(1,13)
        if  (guess == 'h' and  self.value  < self.value2) or (guess == 'l' and self.value > self.value2):
            self.points += 100
        elif (guess == 'h' and  self.value > self.value2) or (guess == 'l' and self.value < self.value2):
            self.points -= 75
        
            



