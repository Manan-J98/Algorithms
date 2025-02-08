class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        res = []
        for index, char in enumerate(s):
            lastIndex[char] = index 
        size, end = 0,0
        for i in range(len(s)):
            end = max(end, lastIndex[s[i]])
            size += 1
            print(end)
            if i == end:
                res.append(size)
                size = 0
        return res
        