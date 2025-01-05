class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shiftArray = [0] * len(s)
        res = ""
        for left, right, shift in shifts:
            direction = -1 if shift == 0 else 1
            shiftArray[left] += direction
            if right+1 < len(s):
                shiftArray[right+1] -= direction
        
        for i in range(1, len(shiftArray)):
            shiftArray[i] += shiftArray[i-1]

        for i in range(len(s)):
            res += chr((ord(s[i]) - ord('a') + shiftArray[i]) % 26 + ord('a'))
        return res
