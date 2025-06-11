class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        freq = defaultdict(int)
        res = 0
        for right in range(len(s)):
            freq[s[right]] += 1
            while self.atLeastOne(freq) and left < right:
                res += len(s) - right
                freq[s[left]] -= 1
                left += 1
        return res
    
    def atLeastOne(self, hashmap) -> bool:
        return hashmap["a"] > 0 and hashmap["b"] > 0 and hashmap["c"] > 0
