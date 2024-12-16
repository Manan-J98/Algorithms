class Solution:
    # greedy approach: always take the minimum element in order to start a group
    # keep a hash map for freq
    # keep a heap to track min val
    # if the val that is popped is not the min val, return False cause hole in group 

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (len(hand) % groupSize) != 0:
            return False
        
        freq = Counter(hand)
        minH = list(freq.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in freq: # check if all values with +1 diff are present
                    return False
                freq[i] -= 1
                if freq[i] == 0:
                    if i != minH[0]: # if min val is not the one being popped
                        return False
                    heapq.heappop(minH)
        return True
                
        
        
