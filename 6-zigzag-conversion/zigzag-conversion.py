class Solution:
    # use simple 2D matrix to create the zigzag pattern
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) < numRows:
            return s
        
        result = ""
        index, direction = 0, 1
        rows = [[] for _ in range(numRows)]
        for char in s:
            rows[index].append(char)
            if index == 0:
                direction = 1
            elif index == numRows - 1:
                direction = -1 # change direction when end is reached 
            index += direction
        for row in rows:
            result += ''.join(row)
        return result
            