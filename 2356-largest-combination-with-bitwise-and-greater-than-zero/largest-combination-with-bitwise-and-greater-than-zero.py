class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bitPos = [0] * 24
        for i in range(len(bitPos)):
            for candidate in candidates:
                bitPos[i] += 1 if (candidate >> i) & 1 == 1 else 0
        return max(bitPos)