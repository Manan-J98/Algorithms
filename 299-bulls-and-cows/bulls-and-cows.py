from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_count = Counter()
        guess_count = Counter()
        
        # First pass to count bulls
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_count[secret[i]] += 1
                guess_count[guess[i]] += 1
        
        # Second pass to count cows
        for digit in guess_count:
            cows += min(secret_count[digit], guess_count[digit])
        
        return f"{bulls}A{cows}B"
