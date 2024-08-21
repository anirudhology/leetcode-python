import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.user_tweets = defaultdict(list)
        self.user_following = defaultdict(set)
        self.tweets_timestamps = defaultdict(int)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append(tweetId)
        self.timestamp += 1
        self.tweets_timestamps[tweetId] = self.timestamp

    def getNewsFeed(self, userId: int) -> List[int]:
        # Get all users that this user follows
        users = self.user_following[userId]
        # Add current user also to this set
        users.add(userId)
        # Get 10 most recent tweets
        tweets = [self.user_tweets[u][::-1][:10] for u in users]
        tweets = sum(tweets, [])
        return heapq.nlargest(10, tweets, key=lambda tweet: self.tweets_timestamps[tweet])

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_following:
            self.user_following[followerId].remove(followeeId)
