class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  # Convert to set for O(1) lookups
        memo = {}  # Dictionary to store already computed results

        def solve(index):
            # If we've reached the end of the string, it's a valid segmentation
            if index == len(s):
                return True

            # If the result is already computed, return it
            if index in memo:
                return memo[index]

            word = ""
            for i in range(index, len(s)):
                word += s[i]
                if word in wordSet and solve(i + 1):  # Recursive call if the word is valid
                    memo[index] = True
                    return True

            # If no valid segmentation is found, store and return False
            memo[index] = False
            return False

        return solve(0)
