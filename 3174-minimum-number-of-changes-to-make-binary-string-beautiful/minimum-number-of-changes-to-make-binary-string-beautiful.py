class Solution:
    def minChanges(self, s: str) -> int:
        i = 0
        changes = 0
        while i+1 < len(s):
            if not s[i] == s[i+1]:
                changes += 1
            i = i + 2
        return changes