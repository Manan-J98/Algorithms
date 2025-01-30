class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # recursive Solution
        # def solve(index, open):
        #     if open < 0:
        #         return False
        #     if index == len(s):
        #         return open == 0
            
        #     if s[index] == "(":
        #         return solve(index+1, open + 1)
        #     elif s[index] == ")":
        #         return solve(index+1, open - 1)
        #     else:
        #         return solve(index+1, open+1) or solve(index+1, open-1) or solve(index+1, open)
        # return solve(0, 0)
        openMin, openMax = 0, 0
        for char in s:
            if char == '(':
                openMin, openMax = openMin + 1, openMax + 1
            elif char == ')':
                openMin, openMax = openMin - 1, openMax - 1
            else:
                openMin, openMax = openMin - 1, openMax + 1
            if openMin < 0:
                openMin = 0
            if openMax < 0:
                return False
        if openMin == 0:
            return True
        return False   
