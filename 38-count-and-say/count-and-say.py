class Solution:
    def count(self, s) -> list:
        res = []
        count = 1
        for i in range(len(s)):
            if i+1 >= len(s):
                res.append([count, int(s[i])])
                break
            if s[i] == s[i+1]:
                count+=1
            else:
                res.append([count, int(s[i])])
                count = 1
        return res

    def say(self, arr) -> str:
        res = ""
        for v1,v2 in arr:
            s = str(v1) + str(v2)
            res += s
        return res


    def countAndSay(self, n: int) -> str:
        start = "1"
        for i in range(n-1):
            count = self.count(start)
            start = self.say(count)
        return start