class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        arr = [i for i in range(1, n+1)]
        def solve(index, out):
            # base case 
            if len(out) == k:
                res.append(out[:])
                return
            for i in range(index, len(arr)):
                out.append(arr[i])
                solve(i+1, out)
                out.pop()
        solve(0, [])
        return res