class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sumMap = {}
        res = -1
        for num in nums:
            dSum = self.getSum(num)
            if dSum in sumMap:
                max1, max2 = sumMap[dSum]
                if num > max1:
                    max2 = max1
                    max1 = num
                elif num > max2:
                    max2 = num
                sumMap[dSum] = (max1, max2)
                res = max(res, max1+max2)
            else:
                sumMap[dSum] = (num, -1)
        print(sumMap)
        return res
        
        
    
    def getSum(self, n) -> int:
        return sum(map(int, str(abs(n))))