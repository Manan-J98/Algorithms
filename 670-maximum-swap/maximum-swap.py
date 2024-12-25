class Solution:
    def maximumSwap(self, num: int) -> int:
        s = [int(val) for val in str(num)]
        maxIndex = len(s)-1
        index1 = index2 = -1 # default case of no swaps

        for i in range(len(s)-1, -1, -1):
            if s[i] > s[maxIndex]:
                maxIndex = i
            elif s[i] < s[maxIndex]:
                index1, index2 = i, maxIndex
        
        if index1 != -1:
            s[index1], s[index2] = s[index2], s[index1]
        return int("".join(map(str, s)))