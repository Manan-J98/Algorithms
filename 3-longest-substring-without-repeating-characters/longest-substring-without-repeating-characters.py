class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = set()
        res = float('-inf')
        left, right = 0,0
        while right < len(s):
            if s[right] not in freq:
                freq.add(s[right])
                right += 1
                res = max(res, right - left)
            else:
                freq.remove(s[left])
                left +=1
        return 0 if res == float("-inf") else res
