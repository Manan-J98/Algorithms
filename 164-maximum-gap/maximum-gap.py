class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        #use bucket sort
        max_num, min_num = max(nums), min(nums) 
        bucket_size = max(1, (max_num - min_num) // (len(nums)-1))
        number_of_buckets = (max_num - min_num) // bucket_size + 1

        buckets = [[float('inf'), float('-inf')] for _ in range(number_of_buckets)]

        for num in nums:
            index = (num-min_num) // bucket_size
            buckets[index][0] = min(num, buckets[index][0])
            buckets[index][1] = max(num, buckets[index][1])
        print(buckets)

        max_gap = 0
        prev_max = min_num

        for bucket in buckets:
            # Skip empty buckets
            if bucket[0] == float('inf') and bucket[1] == float('-inf'):
                continue
            # Calculate the gap between the current bucket's min and the previous max
            max_gap = max(max_gap, bucket[0] - prev_max)
            # Update the previous max for the next gap calculation
            prev_max = bucket[1]

        return max_gap
