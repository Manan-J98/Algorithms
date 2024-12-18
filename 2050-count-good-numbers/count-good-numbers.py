class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7  # Modulus value

        # Total even positions
        even_positions = (n + 1) // 2
        # Total odd positions
        odd_positions = n // 2

        # Calculate the result using modular exponentiation
        result = pow(5, even_positions, MOD) * pow(4, odd_positions, MOD) % MOD
        
        return result
