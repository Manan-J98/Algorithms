class Twitter:

    def __init__(self):
        self.tweets = {}
        self.followers = {}
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId].append((-self.time, tweetId))
        else:
            self.tweets[userId] = [(-self.time, tweetId)]
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        latestTweets = []
        if userId in self.tweets:
            latestTweets += self.tweets[userId].copy()
        if userId in self.followers:
            for f in self.followers[userId]:
                if f in self.tweets:
                    latestTweets += (self.tweets[f])
        heapq.heapify(latestTweets)
        res = []
        while latestTweets and len(res) < 10:
            res.append(heapq.heappop(latestTweets)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].add(followeeId)
        else:
            self.followers[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        else:
            return


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)