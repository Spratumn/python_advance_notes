from collections import namedtuple
import random


Card = namedtuple('Card', ['number', 'shape'])


class Poker:
    numbers = '23456789TJQKA'
    shapes = '♥♠♣♦'
    joker = '小王 大王'.split()

    def __init__(self):
        self._cards = [Card(n, s) for n in Poker.numbers for s in Poker.shapes]
        self._cards.append(Card(15, Poker.joker[0]))
        self._cards.append(Card(16, Poker.joker[1]))

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __repr__(self):
        return str(self._cards)


if __name__ == '__main__':
    deck = Poker()
    print(len(deck))
    print(deck[19])
    print(deck[10:19])

    print('*'*8)
    for _ in range(8):
        print(random.choice(deck))

    print(deck)
    random.shuffle(deck)
    print(deck)
