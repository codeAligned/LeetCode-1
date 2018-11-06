# 933. Number of Recent Calls
# Time: O(log(N))
# Space: O(N)

# use bisect_left to find all(val >= t - 3000 for val in self.pings[idx:])
class RecentCounter(object):

    def __init__(self):
        self.pings = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.pings.append(t)
        idx = bisect.bisect_left(self.pings, t - 3000)
        self.pings = self.pings[idx:]
        return len(self.pings)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# Time: O(N)
# Space: O(N)

# maintain the queue for each incoming ping and return the size
from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.pings = deque([])

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        if not self.pings:
            self.pings.append(t)
        else:
            while self.pings and t - 3000 > self.pings[0]:
                self.pings.popleft()
            self.pings.append(t)
        return len(self.pings)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)