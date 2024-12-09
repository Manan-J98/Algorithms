class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        fp, sp = 0, 0
        res = 0
        while sp < len(s) and fp < len(g):
            print(sp, fp)
            if s[sp] >= g[fp]:
                res += 1
                sp += 1
                fp += 1
            else:
                sp += 1
        return res
            