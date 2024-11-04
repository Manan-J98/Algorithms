class Solution:
    def compressedString(self, word: str) -> str:
        start, end = 0, 0
        res = ""
        while end < len(word):
            if word[start] == word[end]:
                end += 1
            else:
                while (end - start) > 9:  # Process chunks of 9 if length exceeds 9
                    res += "9" + word[start]
                    start += 9
                res += str(end - start) + word[start]
                start = end
            # Ensure end moves forward correctly
        while (end - start) > 9:
            res += "9" + word[start]
            start += 9
        if start < end:  # Final part for leftover characters
            res += str(end - start) + word[start]
        return res