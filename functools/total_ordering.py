from functools import total_ordering
import random



@total_ordering
class Hero:
    def __init__(self, name,  live=None, magic=None):
        self.name = name
        self.live = live or random.randint(0, 100)
        self.magic = magic or random.randint(0, 100)

    def __lt__(self, other):
        return (self.live, self.magic) < (other.live, other.magic)

    def __eq__(self, other):
        return (self.live, self.magic) == (other.live, other.magic)


print(Hero('libai', 10, 10) == Hero('caocao', 10, 10)) # True
print(Hero('libai', 11, 12) >= Hero('caocao', 10, 13)) # True