class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        rows = {0: []}
        curKey = 0
        for num in nums:
            didAppend = False
            for key, val in rows.items():
                if num not in rows[key]:
                    rows[key].append(num)
                    didAppend = True
                    break
            if not didAppend:
                curKey += 1
                rows[curKey] = [num]
        return [val for val in rows.values()]