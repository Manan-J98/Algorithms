class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if not sentence[0] == sentence[-1]:
            return False
        for i in range(0, len(sentence)):
            if sentence[i] == " ":
                if not sentence[i-1] == sentence[i+1]:
                    return False
        return True
                
