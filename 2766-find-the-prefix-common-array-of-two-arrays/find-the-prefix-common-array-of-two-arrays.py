class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        uni = set()
        matches = 0
        res = []
        for i in range(len(A)):
            if A[i] in uni:
                matches += 1
            uni.add(A[i])
            if B[i] in uni:
                matches += 1
            uni.add(B[i])
            res.append(matches)
        return res