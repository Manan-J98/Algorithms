class Solution:
    def isFascinating(self, n: int) -> bool:
        mod = str(n) + str(2*n) + str(3*n)
        digits = [0] * 9
        nums = [int(char) for char in mod]
        print(nums)
        for num in nums:
            if digits[num-1] != 0:
               return False
            elif num != 0:
                digits[num-1] += 1
        print(digits)
        for digit in digits:
            if digit != 1:
                return False
        return True     