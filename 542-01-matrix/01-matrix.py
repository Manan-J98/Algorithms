class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        result = [[0] * len(mat[0]) for _ in range(len(mat))]
        visited = set()
        def bfs():
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    X = x + dx
                    Y = y + dy
                    if inBounds(X, Y) and mat[X][Y] == 1 and (X,Y) not in visited:
                        result[X][Y] = result[x][y] + 1
                        visited.add((X,Y))
                        q.append((X,Y))

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
                
        def inBounds(x, y):
            if x < 0 or y < 0 or x >= len(mat) or y >= len(mat[0]):
                return False
            return True

        bfs()
        return result
                        
        

