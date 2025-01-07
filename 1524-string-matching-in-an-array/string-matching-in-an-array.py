class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words = sorted(words, key=len)
        print(words)
        res = []
        for i in range(len(words)-1):
            if words[i] in "#".join(words[i+1:]):
                res.append(words[i])
        return res