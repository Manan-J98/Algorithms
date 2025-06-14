class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indexMap = {}
        for index, char in enumerate(s):
            if char in indexMap:
                indexMap[char].append(index)
            else:
                indexMap[char] = [index]
        res = 0
        for word in words:
            lastIndex = -1
            noResult = False
            for char in word:
                if char not in indexMap:
                    noResult = True
                    break
                search = self.search(lastIndex, indexMap[char])
                if search is not None:
                    lastIndex = search
                else:
                    noResult = True
                    break
            if not noResult:
                res += 1
        return res

    def search(self, lastIndex, arr):
        start, end = 0, len(arr)-1
        res = None
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] > lastIndex:
                res = arr[mid]
                end = mid - 1
            else:
                start = mid + 1
        return res