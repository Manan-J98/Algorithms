class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        freq = Counter(s)

        for char, f in freq.items():
            heapq.heappush(heap, (-f, char))
        
        prev = (0, "")
        res = ""
        while heap:
            f, char = heapq.heappop(heap)
            res += char
            if prev[0] < 0:
                heapq.heappush(heap, prev)
            prev = (f+1, char)
        return res if len(res) == len(s) else ""