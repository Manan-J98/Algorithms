class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        def solve(index, out):
            # base case 
            if index == len(s):
                ans.append(" ".join(out[:]))
                return
            word = ""
            for i in range(index, len(s)):
                word += s[i]
                if word in wordDict:
                    out.append(word)
                    solve(i+1, out)
                    out.pop()
        solve(0, [])
        return ans