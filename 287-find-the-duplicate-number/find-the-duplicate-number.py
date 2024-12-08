class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # Floyd's Algorithm 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # think of it as pointers, fast points to the .next.next of node
            if slow == fast: # now we need the val that pointed to this index
                break
        print(slow, fast)
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

        
