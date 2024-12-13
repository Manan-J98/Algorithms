from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        curWidth = 0
        curLine = 1
        
        for char in s:
            charWidth = widths[ord(char) - ord('a')]
            if curWidth + charWidth > 100:
                curLine += 1
                curWidth = charWidth
            else:
                curWidth += charWidth
        
        return [curLine, curWidth]
