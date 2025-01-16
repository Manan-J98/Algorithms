class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # stores tuples (val, index)
        for i in range(len(temperatures)):
            
            while stack and temperatures[i] > stack[-1][0]:
                val, index = stack.pop()
                res[index] = i - index
            stack.append((temperatures[i], i))
        return res
