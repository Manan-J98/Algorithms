class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users = {}
        for log in logs:
            userId, time = log[0], log[1]
            if userId in users:
                users[userId].add(time)
            else:
                users[userId] = set()
                users[userId].add(time)
        res = [0] * k
        for user in users:
            res[len(users[user])-1] += 1
        return res