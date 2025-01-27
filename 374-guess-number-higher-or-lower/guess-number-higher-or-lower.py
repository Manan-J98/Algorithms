# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        curGuess = (l + r) // 2
        res = 0
        while l <= r:
            if guess(curGuess) == 0:
                res = curGuess
                return res
            if guess(curGuess) == 1:
                l = curGuess + 1
            else:
                r = curGuess - 1
            curGuess = (l + r) // 2
        return res
