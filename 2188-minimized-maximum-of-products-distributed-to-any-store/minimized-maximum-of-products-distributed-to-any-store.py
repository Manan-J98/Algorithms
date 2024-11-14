class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistribute(p):
            storesReq = 0
            for q in quantities:
                storesReq += ceil(q/p) # min stores req with given mid (distribution val)
            return storesReq <= n

        l,r = 1, max(quantities)
        res = r
        while l <= r:
            mid = (l + r) // 2
            if canDistribute(mid):
                res = mid
                r = mid - 1 # keep searching for lower possible answer
            else: # increase min q to distribute
                l = mid + 1
        return res
            