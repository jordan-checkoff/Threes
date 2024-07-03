from Card import Card
import random

class CardFactory:

    def createCard(self, val):
        return Card(val)
    
    def createRandomCard(self):
        val = random.randint(1,3)
        return self.createCard(val)