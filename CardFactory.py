from Card import Card
import random

class CardFactory:

    def create_card(self, val):
        if val:
            return Card(val)
        else:
            return None
    
    def create_random_card(self, turn):
        val = random.randint(1,3)
        return self.create_card(val)