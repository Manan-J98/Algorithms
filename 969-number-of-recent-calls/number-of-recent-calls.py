class RecentCounter:

    def __init__(self):
        self.timestamp = deque()

    def ping(self, t: int) -> int:
        # Add the new timestamp
        self.timestamp.append(t)
        
        # Remove timestamps that are outside the 3000ms window
        while self.timestamp and self.timestamp[0] < t - 3000:
            self.timestamp.popleft()
        
        # The size of the deque is the number of valid pings
        return len(self.timestamp)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)