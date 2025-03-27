class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums)
        dom, maxFreq = 0, 0
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            
            if freq[num] > maxFreq:
                    maxFreq = freq[num]
                    dom = num
        print(dom, maxFreq)
        f1 = 0
        for i in range(n-1):
            if nums[i] == dom:
                f1 += 1
                maxFreq -=1
            print(f1, maxFreq, i, n)
            if (f1 > (i+1)/2) and (maxFreq > (n-(i+1))/2):
                return i
        return -1

