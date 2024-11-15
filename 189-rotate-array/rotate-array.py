class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)  # Handle cases where k > len(nums)
        temp = nums[:]  # Make a copy of nums to preserve original values

        for index in range(len(nums)):
            nums[(index + k) % len(nums)] = temp[index]  # Assign values from the copy



        
        