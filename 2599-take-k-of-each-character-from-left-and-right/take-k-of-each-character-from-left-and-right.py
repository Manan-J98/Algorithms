class Solution:
    # get total freq of a, b and c
    # create a valid sliding window where all characters in the window can be removed safely while maintaing min count
    # goal is to kinda slide window till the middle (optimal ans) and remove the max valid window from total size

    def takeCharacters(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
            
        for char in "abc":
            if freq[char] < k:
                return -1

        left = 0
        curSize, maxSize = 0, 0
        window = defaultdict(int)
        for r in range(len(s)):
            window[s[r]] += 1

            while True:
                valid = True
                for key in "abc":
                    if freq[key] - window[key] < k:
                        valid = False
                        break
                if valid:
                    break
                window[s[left]] -= 1
                left += 1
            
            curSize = r - left + 1
            maxSize = max(maxSize, curSize)
        return len(s)-maxSize
            

            
        