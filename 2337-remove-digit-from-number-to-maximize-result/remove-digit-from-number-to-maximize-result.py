class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxNum = float("-inf")
        for i in range(len(number)):
            if number[i] == digit:
                res = number[:i] + number[i+1:]
                maxNum = max(int(res), maxNum)
        return str(maxNum)