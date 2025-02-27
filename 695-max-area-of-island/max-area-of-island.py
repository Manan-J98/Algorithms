class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = [0]
        visited = set()

        def bfs(r, c):
            # implement
            q = deque()
            dirs = [[1,0], [0,-1], [-1,0], [0,1]]
            q.append((r,c))
            visited.add((r,c))
            temp = 1
            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 1 and
                        (r, c) not in visited):
                        temp += 1
                        q.append((r,c))
                        visited.add((r,c))
            area[0] = max(area[0], temp)
                    
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    bfs(r,c)
        return area[0]

        