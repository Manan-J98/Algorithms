class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            # Helper function to count the frequency of characters in a word
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            return freq
        
        # Calculate the combined maximum frequency for words2
        combinedFreq = [0] * 26
        for word in words2:
            for i, freq in enumerate(count(word)):
                combinedFreq[i] = max(combinedFreq[i], freq)
        
        # Find universal words in words1
        res = []
        for word in words1:
            wordFreq = count(word)
            if all(wordFreq[i] >= combinedFreq[i] for i in range(26)):
                res.append(word)
        
        return res
            
