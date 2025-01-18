class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums2)
        out = []
        stack = [] # store tuples
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1][0]:
                val, index = stack.pop()
                res[index] = nums2[i]
            stack.append((nums2[i], i))
        for num in nums1:
            out.append(res[nums2.index(num)])
        return out