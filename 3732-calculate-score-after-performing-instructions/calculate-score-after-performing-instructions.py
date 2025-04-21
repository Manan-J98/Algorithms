class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        indexSet = set()
        i = 0
        score = 0
        n = len(instructions)

        while 0 <= i < n:
            if i in indexSet:
                break
            indexSet.add(i)

            if instructions[i] == "add":
                score += values[i]
                i += 1
            else:
                i += values[i]

        return score
