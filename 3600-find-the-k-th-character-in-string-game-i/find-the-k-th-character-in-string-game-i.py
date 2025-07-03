class Solution:
    def kthCharacter(self, k: int) -> str:
        
        def solve(word):
            if len(word) > k:
                return word[k-1]
            return solve(self.perform(word))
        return solve("a")
        
    def perform(self, word):
        newWord = ''.join([chr(ord(c)+1) for c in word])
        return word + newWord