# Time Complexity: O(1), Space Complexity: O(N)

import random


class RandomizedSet:

    def __init__(self):
        self.values = []
        self.idx_map = {}
        

    def insert(self, val: int) -> bool:
        if val in self.idx_map:
            return False
        self.values.append(val)
        self.idx_map[val] = len(self.values) - 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.idx_map:
            return False
        
        idx = self.idx_map[val]
        last_val = self.values[-1]

        self.values[idx] = last_val
        self.idx_map[last_val] = idx

        self.values.pop()
        del self.idx_map[val]

        return True
        

    def getRandom(self) -> int:
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
