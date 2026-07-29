import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        is_new = len(self.idx[val]) == 0

        self.idx[val].add(len(self.nums))
        self.nums.append(val)

        return is_new

    def remove(self, val: int) -> bool:
        if not self.idx[val]:
            return False

        # Get an index of val to remove
        remove_idx = self.idx[val].pop()

        last_val = self.nums[-1]
        last_idx = len(self.nums) - 1

        # If removing is not the last element, swap
        if remove_idx != last_idx:
            self.nums[remove_idx] = last_val

            self.idx[last_val].remove(last_idx)
            self.idx[last_val].add(remove_idx)

        self.nums.pop()

        if not self.idx[val]:
            del self.idx[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)