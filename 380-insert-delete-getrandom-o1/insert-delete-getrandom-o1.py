class RandomizedSet:

    def __init__(self):
        self.randSet = {}

    def insert(self, val: int) -> bool:
        if val not in self.randSet:
            self.randSet[val] = val
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.randSet:
            del self.randSet[val]
            return True
        return False

    def getRandom(self) -> int:
        rand = random.choice(list(self.randSet.keys()))
        return self.randSet[rand]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()