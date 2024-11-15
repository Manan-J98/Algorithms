class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def solve(ip, out):
            if not ip:
                res.append(out.copy())
                return
            out.append(ip[0])
            solve(ip[1:], out)

            # backtrack for choice 2 to exclude element
            out.pop()
            solve(ip[1:], out)
        solve(nums, [])
        return res
            
