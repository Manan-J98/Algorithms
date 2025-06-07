class Solution:

    def clearStars(self, s: str) -> str:
        stack = []
        heap = []
        deleted = set()

        for index, char in enumerate(s):
            if char == "*":
                while heap:
                    c, i = heapq.heappop(heap)
                    i = -i
                    if i not in deleted:
                        deleted.add(i)
                        break
            else:
                stack.append((char, index))
                heapq.heappush(heap, (char, -index))
        
        # Rebuild the result by skipping deleted indices
        result = []
        for c, i in stack:
            if i not in deleted:
                result.append(c)
        return ''.join(result)