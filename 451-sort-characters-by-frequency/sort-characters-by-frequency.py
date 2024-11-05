class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        heapify(heap)
        freq = defaultdict(int)
        res = ""
        for char in s:
            freq[char] += 1
            
        
        for key, val in freq.items():
            heappush(heap, (-val,key))

        while heap:
            val = heappop(heap)
            res += -val[0] * val[1]  
        return res
        # return "".join([t * -count for (count, t) in heap]) # does not maintain order unless popped
