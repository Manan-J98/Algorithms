class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        count = 0
        for num in range(1, n+1):
            if n % num == 0:
                factors.append(num)
                count += 1
                if count == k:
                    return num
        print(factors)
        return -1