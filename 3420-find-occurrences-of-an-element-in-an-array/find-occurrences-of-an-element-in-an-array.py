class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        indexMap = {}
        for index, val in enumerate(nums):
            if val in indexMap:
                indexMap[val].append(index)
            else:
                indexMap[val] = [index]
        res = []
        print(indexMap)
        for query in queries:
            if x not in indexMap:
                res.append(-1)
            elif len(indexMap[x]) < query:
                res.append(-1)
            else:
                res.append(indexMap[x][query-1])
        return res