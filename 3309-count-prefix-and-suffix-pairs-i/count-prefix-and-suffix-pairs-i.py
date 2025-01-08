class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    res += 1
        return res

    def isPrefixAndSuffix(self, a, b) -> bool:
        size = len(a)
        print(b[0:size], b[-size:])
        if size > len(b):
            return False
        elif b[0:size] == a and b[-size:] == a:
            return True
        return False