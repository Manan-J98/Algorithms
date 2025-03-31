class Solution:
    def reverse(self, x: int) -> int:
       mini, maxi = -int(math.pow(2, 31)), int(math.pow(2,31))
       num = str(abs(x))
       num = int(num[::-1])
       if num not in range(mini, maxi):
            return 0
       return -num if x < 0 else num



