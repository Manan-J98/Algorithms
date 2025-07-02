class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dirs = [(1,0), (0,-1), (-1,0), (0,1)]
        visited = set()
        minHeap = [(grid[0][0], 0, 0)]
        maxElevation = -1
        while minHeap:
            elevation, x, y = heapq.heappop(minHeap)
            maxElevation = max(maxElevation, elevation)
            if x == len(grid)-1 and y == len(grid[0])-1:
                return maxElevation
            for dx, dy in dirs:
                X = x + dx
                Y = y + dy
                if self.inBounds(grid, X, Y) and (X,Y) not in visited:
                    heapq.heappush(minHeap, (grid[X][Y], X, Y))
                    visited.add((x, y))
        return maxElevation
    
    def inBounds(self, grid, x, y) -> bool:
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        return True
        