class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = [] 
        temp = ""
        for char in s:
            temp += char
            if len(temp) == k:
                res.append(temp)
                temp = ""
        if len(temp) > 0:
            temp += (k - len(temp)) * fill
            res.append(temp)
        return res