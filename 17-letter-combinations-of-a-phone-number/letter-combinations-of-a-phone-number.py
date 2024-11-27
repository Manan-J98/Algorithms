class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneMap = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        def solve(index, out):
            if index == len(digits):
                if out:
                    res.append(out)
                return 
            
            letters = phoneMap[digits[index]]
            for char in letters:
                solve(index+1, out+char) # solve for every char in letters and combine through recursion
        
        solve(0, "")
        return res

