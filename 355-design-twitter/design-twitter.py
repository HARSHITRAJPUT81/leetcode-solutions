from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int):
        res = []
        heap = []

        # User always follows themselves
        self.followMap[userId].add(userId)

        for followee in self.followMap[userId]:
            tweets = self.tweetMap[followee]
            if tweets:
                idx = len(tweets) - 1
                time, tweetId = tweets[idx]
                heapq.heappush(heap, (-time, tweetId, followee, idx - 1))

        while heap and len(res) < 10:
            negTime, tweetId, user, idx = heapq.heappop(heap)
            res.append(tweetId)

            if idx >= 0:
                time, tid = self.tweetMap[user][idx]
                heapq.heappush(heap, (-time, tid, user, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.followMap[followerId].discard(followeeId)