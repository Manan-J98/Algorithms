class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        adj = defaultdict(list)
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))
        maxScore = [0]    
        visitedCount = defaultdict(int)
        def dfs(node, elapsedTime, currentScore):
            if elapsedTime > maxTime:
                return
            
            if visitedCount[node] == 0:
                currentScore += values[node]
            visitedCount[node] += 1

            if node == 0:
                maxScore[0] = max(maxScore[0], currentScore)

            for nei, time in adj[node]:
                dfs(nei, elapsedTime + time, currentScore)
            
            visitedCount[node] -= 1
        
        dfs(0, 0, 0)
        return maxScore[0]
            