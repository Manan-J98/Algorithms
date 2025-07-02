class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        res = []
        def dfs(src):
            while adj[src]:
                curr = adj[src].pop()
                dfs(curr)
            res.append(src)
        dfs("JFK")
        return res[::-1]