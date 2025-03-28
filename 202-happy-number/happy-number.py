class Solution:
    def isHappy(self, n: int) -> bool:
        hashSet = set()
        curSum = n
        while curSum not in hashSet:
            hashSet.add(curSum)
            curSum = self.digitSum(curSum)
            if curSum == 1:
                return True
        return False


    def digitSum(self, n):
        digits = str(n)
        return sum([(int(char) * int(char)) for char in digits])