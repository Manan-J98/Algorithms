class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        res = []
        ans = []
        for row in range(len(score)):
            res.append((score[row][k], row))
        res = sorted(res, reverse = True)
        print(res)
        for row in range(len(score)):
            ans.append(score[res[row][1]])
        return ans