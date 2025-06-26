class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        binLen = len(bin(k).split("0b")[1])
        strLen = len(s)
        if binLen >= strLen:
            return strLen
        res = 0
        val, bit = 0, 1
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                res += 1
            else:
                if val + bit <= k:
                    val += bit
                    res += 1
            bit *= 2
        return res
            