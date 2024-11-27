# main intuition - mcm pattern
# keep moving swap positions
# basically two options, either swap or don't 
# when swapped, check first part of string with last part of swapped string 
# same for last part of string with first part of swapped string
# when not swapped, check first part with corresponding first part
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        memo = {}
        def check(a, b):
            if (a,b) in memo:
                return memo[(a,b)]
            if a == b:
                memo[(a,b)] = True
                return True
            if len(a) <= 1: # breaking is not possible where one string is empty so length has to be > 1 so that it can be compared with b
                return False
            n = len(a)
            flag = False
            for i in range(1, n): # break at every i possible
                # Case 1: Without swapping
                if check(a[:i], b[:i]) and check(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True
                # Case 2: With swapping
                if check(a[:i], b[-i:]) and check(a[i:], b[:-i]):
                    memo[(a, b)] = True
                    return True
            memo[(a, b)] = False
            return False
        return check(s1, s2)

