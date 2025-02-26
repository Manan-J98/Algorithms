class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            # implement
            q = deque()
            dirs = [[1,0], [0,-1], [-1,0], [0,1]]
            q.append((r,c))
            visited.add((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))

    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    # mark all the "1"s visited
                    bfs(r,c)
                    islands += 1
        return islands
        