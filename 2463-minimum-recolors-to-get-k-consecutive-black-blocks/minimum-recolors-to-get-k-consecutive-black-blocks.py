class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = 0
        for i in range(k):
            if blocks[i] == "W":
                res += 1
        print(res)
        i, j= 1, k
        temp = res
        while j < len(blocks):
            if blocks[i-1] == "W":
                temp -= 1
            if blocks[j] == "W":
                temp += 1
            res = min(res, temp)
            i += 1
            j += 1
        return res
            