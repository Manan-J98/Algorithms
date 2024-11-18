from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        res = []
        start, end = (1, k) if k > 0 else (k, -1) # condition for first element. -1 is last elmt index

        curSum = sum([code[i % n] for i in range(start, end+1)])

        for i in range(n):
            res.append(curSum)
            curSum -= code[(i+start) % n]
            curSum += code[(i+end+1) % n]
        return res

