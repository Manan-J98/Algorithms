class Solution:
    def splitNum(self, num: int) -> int:
        numbers = str(num)
        numbers = sorted(numbers)
        i, j = 0, 1
        num1 = num2 = ""
        while i < len(numbers):
            num1 += numbers[i]
            i += 2
        while j < len(numbers):
            num2 += numbers[j]
            j += 2
        return int(num1) + int(num2)