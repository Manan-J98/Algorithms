class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = [0] * 60
        res = 0

        for t in time:
            rem = t % 60
            comp = (60 - rem) % 60
            res += count[comp]
            count[rem] += 1
        return res