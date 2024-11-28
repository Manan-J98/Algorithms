class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        noteFreq = Counter(ransomNote)
        magFreq = Counter(magazine)

        for key in noteFreq.keys():
            if key not in magFreq or magFreq[key] < noteFreq[key]:
                return False
        return True