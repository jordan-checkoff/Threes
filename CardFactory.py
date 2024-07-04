from Card import Card
import random

class CardFactory:

    def create_card(self, val):
        return Card(val)
    
    def create_random_card(self):
        val = random.randint(1,3)
        return self.create_card(val)