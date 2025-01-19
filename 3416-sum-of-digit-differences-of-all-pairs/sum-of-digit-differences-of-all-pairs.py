class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        numStr = [str(num) for num in nums]
        result = 0
        for i in range(len(numStr[0])):
            digit_count = [0] * 10  # Count digits 0-9 for this position

        # Count occurrences of each digit at the current position
            for num in numStr:
                digit = int(num[i])
                digit_count[digit] += 1

            # Compute contributions for this position
            for c in digit_count:
                result += c * (len(numStr) - c)
        return result // 2
