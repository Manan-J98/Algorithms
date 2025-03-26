class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = [num for row in grid for num in row]
        res = 0
        arr.sort()
        median = arr[len(arr)//2]
        for num in arr:
            diff = abs(num-median)
            if diff % x != 0:
                return -1
            else:
                res += abs((num-median)/x)
        return int(res)

