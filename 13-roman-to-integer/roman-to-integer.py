class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D':500, 'M':1000}
        lastChar = None
        res = 0
        for char in s:
            if not lastChar:
                res += roman[char]
            else:
                if roman[lastChar] < roman[char]:
                    res -= roman[lastChar]
                    res += roman[char]-roman[lastChar]
                else:
                    res += roman[char]
            lastChar = char
        return res
                
        