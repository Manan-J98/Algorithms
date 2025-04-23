class Solution:
    def countLargestGroup(self, n: int) -> int:
        sumMap = {}
        maxLen = float("-inf")
        for i in range(1, n+1):
            digiSum = sum(int(char) for char in str(i))
            if  digiSum in sumMap:
                sumMap[digiSum].append(i)
            else:
                sumMap[digiSum] = [i]
            maxLen = max(maxLen, len(sumMap[digiSum]))

        return sum(1 for value in sumMap.values() if len(value) == maxLen)
