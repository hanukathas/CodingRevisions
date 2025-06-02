import random


class RandomizedSet:

    def __init__(self):
        self.randomized_set = set()

    def insert(self, val: int) -> bool:
        if val not in self.randomized_set:
            self.randomized_set.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.randomized_set:
            self.randomized_set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        if len(self.randomized_set) > 0:
            return random.choice(list(self.randomized_set))

    def print_set(self):
        print(self.randomized_set)

if __name__ == '__main__':
    rset = RandomizedSet()
    op = list()

    op.append(rset.insert(1))
    op.append(rset.remove(2))
    op.append(rset.insert(2))
    op.append(rset.getRandom())
    op.append(rset.remove(1))
    op.append(rset.insert(2))
    op.append(rset.getRandom())
    print(op)

