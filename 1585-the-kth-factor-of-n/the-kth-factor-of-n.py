class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        count = 0
        for num in range(1, (n//2) + 1):
            if n % num == 0:
                factors.append(num)
        factors.append(n)
        print(factors)
        return factors[k-1] if k <= len(factors) else -1