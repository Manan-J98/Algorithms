class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        bWords = set(banned)
        freq = defaultdict(int)
        res = ""
        curMax = 0
        words = re.findall(r'\w+', paragraph.lower())
        for word in words:
            w = word.lower()
            if w not in bWords:
                freq[w] += 1
        
        for key, val in freq.items():
            if val > curMax:
                curMax = val
                res = key
        return res