class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        leftArray, rightArray = [], deque()
        for num in nums:
            if num == pivot:
                rightArray.appendleft(num)
            elif num < pivot:
                leftArray.append(num)
            else:
                rightArray.append(num)
        return leftArray + list(rightArray)