class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]
        curGroup = groups[0]
        for i in range(1, len(words)):
            if groups[i] != curGroup:
                res.append(words[i])
                curGroup = groups[i]
        return res
