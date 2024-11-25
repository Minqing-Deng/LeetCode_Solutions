import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.allUsers = set()  # (userId1, ...)
        self.followed = {}  # userId1: (all the userIds that userId1 followed)
        self.tweets = {}  # userId: [(ranking, tweetId1), ...]
        self.ranking = 0

    def addID(self, userId: int) -> None:
        self.allUsers.add(userId)
        self.followed[userId] = set()
        self.tweets[userId] = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.allUsers:
            self.addID(userId)

        self.ranking += 1
        self.tweets[userId].append((self.ranking, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []

        if userId in self.allUsers:
            # Min-heap to store up to 10 most recent tweets
            min_heap = []
            # Add user's own tweets
            for tweet in self.tweets[userId]:
                heapq.heappush(min_heap, tweet)
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)
            # Add followees' tweets
            for followee in self.followed[userId]:
                for tweet in self.tweets[followee]:
                    heapq.heappush(min_heap, tweet)
                    if len(min_heap) > 10:
                        heapq.heappop(min_heap)

            # Extract tweets in descending order of ranking
            while min_heap:
                res.append(heapq.heappop(min_heap)[1])

        return res[::-1]  # Reverse to get the correct order

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.allUsers:
            self.addID(followerId)
        if followeeId not in self.allUsers:
            self.addID(followeeId)
        if followeeId != followerId:  # Prevent self-following
            self.followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.allUsers and followeeId in self.allUsers:
            self.followed[followerId].discard(followeeId)

        # Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)