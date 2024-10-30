class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def solve(n,out, openCount, closeCount):
            if openCount == closeCount == n:
                res.append(out)
                return
            if openCount < n:
                op = out + "("
                solve(n, op, openCount+1, closeCount)
            if closeCount < openCount and closeCount < n:
                op = out + ")"
                solve(n, op, openCount, closeCount+1)
        solve(n, "", 0, 0)
        return res