class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        ans = 0
        for d in s:
            freq[d] += 1
            times1 = min(freq["N"], freq["S"], k)
            times2 = min(freq["W"], freq["E"], k - times1)
            ans = max(ans, self.manDis(freq["N"], freq["S"], times1) + self.manDis(freq["W"], freq["E"], times2))
        return ans

    def manDis(self, d1, d2, times):
        return ( abs(d1 - d2) + times * 2)
