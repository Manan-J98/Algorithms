class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        res = 0
        hasOdd = False
        
        for val in freq.values():
            if val % 2 == 0:
                res += val
            else:
                res += val - 1
                hasOdd = True
        
        # Add one more character if there's at least one odd frequency
        if hasOdd:
            res += 1
            
        return res

        