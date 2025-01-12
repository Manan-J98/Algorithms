class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        balance = 0
        if len(s) % 2 != 0:
            return False
        
        # first pass left to right
        for i in range(len(s)):
            # treat unlocked as '(' cause extra closing means instant False
            if s[i] == "(" or locked[i] == "0":
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                return False
        
        balance = 0
        for i in range(len(s)-1, -1, -1):
            # treat unlocked as ')' cause extra opening means instant False
            if s[i] == ")" or locked[i] == "0":
                balance += 1
            else:
                balance -= 1
                
            if balance < 0:
                return False
        return True
            