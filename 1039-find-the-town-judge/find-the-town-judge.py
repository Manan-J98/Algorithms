class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)
        for t in trust:
            outgoing[t[0]] += 1
            incoming[t[1]] += 1
        for i in range(1, n+1):
            if incoming[i] == n-1 and outgoing[i] == 0:
                return i
        return -1