class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        indexMapper = defaultdict(int)
        minVal = float('inf')
        res = []
        for index, word in enumerate(list1):
            indexMapper[word] = index
        
        for index, word in enumerate(list2):
            if word in indexMapper:
                indexMapper[word] += index
                if indexMapper[word] < minVal:
                    res = [word]
                    minVal = indexMapper[word]
                elif indexMapper[word] == minVal:
                    res.append(word)
        return res