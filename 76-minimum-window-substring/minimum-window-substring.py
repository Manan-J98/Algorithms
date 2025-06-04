class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounter = Counter(t)
        req = len(tCounter.keys())
        have = 0
        left, right = 0, 0
        res = [-1, -1]
        resLen = float('inf')
        window = defaultdict(int)
        while right < len(s):
            char = s[right]
            window[char] += 1
            if char in tCounter and window[char] == tCounter[char]: # this means we have the needed amount
                have += 1
            while have == req:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                c = s[left]
                window[c] -= 1
                if window[c] < tCounter[c]:
                    have -= 1
                left += 1
            right += 1
        return s[res[0]:res[1]+1] if (resLen != float('inf')) else ""

            