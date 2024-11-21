class Solution:
    # two choices, either take 1 number or take 2
    def numDecodings(self, s: str) -> int:
        memo = {}
        def decode(index):
            # base case 
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            
            if index in memo:
                return memo[index]
            # decode 1 char
            result = decode(index + 1)

            # decode 2 if valid 
            if index + 1 < len(s) and 10 <= int(s[index:index+2]) <= 26:
                result += decode(index+2)
            
            memo[index] = result
            return result
        return decode(0)