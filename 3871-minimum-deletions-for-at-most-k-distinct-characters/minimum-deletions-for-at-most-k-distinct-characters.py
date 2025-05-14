class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freqArray = [0] * 26
        for char in s:
            freqArray[ord(char)-ord('a')] += 1
        freqArray.sort(reverse=True)
        return sum(freqArray[k:])
        