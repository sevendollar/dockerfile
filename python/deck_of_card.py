class DeckOfCard:
    def __init__(self):
        self.nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
        self.suits = ['clubs', 'diamonds', 'heats', 'spades']
        self.doc = []
        for suit in self.suits:
            for num in self.nums:
                self.doc.append(num + ' of ' + suit)

    def random_deliver(self):
        import random
        return self.doc.pop(random.randrange(len(self.doc)))

    def show(self):
        return self.doc

suit = DeckOfCard()
players = {}
player_num = 4
num_of_delivers = 4
# for num in range(player_num):
#     players.setdefault(('player%s' % num), [])
#     for _ in range(num_of_deliver):
#         players[('player%s' % num)] = players[('player%s' % num)] + [suit.random_deliver()]


for x in range(num_of_delivers):
    for y in range(player_num):
        players.setdefault(('player%s' % y), [])
        players[('player%s' % y)] = players[('player%s' % y)] + [suit.random_deliver()]


print(players.get('player0', None))
print(players.get('player1', None))
print(players.get('player2', None))
print(players.get('player3', None))
