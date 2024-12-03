class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        ht = set()
        for val in arr:
            if val*2 in ht or val/2 in ht:
                return True
            else:
                ht.add(val)
        return False