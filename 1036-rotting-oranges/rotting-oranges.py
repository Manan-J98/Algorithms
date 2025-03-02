class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        res = 0
        fresh_count = 0
        def addRottenOrange(r, c):
            if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] == 1:
                grid[r][c] = 2
                visited.add((r,c))
                q.append([r,c])
                return True
            return False

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c]) # add all rotten oranges at once
                    visited.add((r,c)) # rotten cells are already visited
                elif grid[r][c] == 1:
                    fresh_count += 1

        # If no fresh oranges exist, return 0 immediately
        if fresh_count == 0:
            return 0

        isRotten = False
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                top = addRottenOrange(r-1, c)
                bottom = addRottenOrange(r+1, c)
                left = addRottenOrange(r, c-1)
                right = addRottenOrange(r, c+1)

                if any([top, bottom, left, right]):
                    isRotten = True
            if isRotten:
                res += 1
                isRotten = False

        print(grid)
        all_rotten = all((cell == 2 or cell == 0) for row in grid for cell in row)
        return res if all_rotten else -1

