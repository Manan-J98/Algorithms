class Solution:
    def reverseWords(self, s: str) -> str:
        first, last = 0, 0
        s = s.strip()
        res = []
        while last < len(s):
            while first < len(s) and s[first] == " ":
                first += 1
            else:
                last = first
                while last < len(s) and s[last] != " ":
                    last += 1
                res.append(s[first:last])
                first = last
        return " ".join(res[::-1])


