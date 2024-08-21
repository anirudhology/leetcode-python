import unittest

from problems.design.design_twitter import Twitter


class TwitterTest(unittest.TestCase):

    def setUp(self):
        self.twitter = Twitter()

    def test_post_tweet(self):
        self.twitter.postTweet(1, 101)
        feed = self.twitter.getNewsFeed(1)
        self.assertEqual(feed, [101])

    def test_get_news_feed(self):
        self.twitter.postTweet(1, 101)
        self.twitter.postTweet(2, 102)
        self.twitter.follow(1, 2)
        feed = self.twitter.getNewsFeed(1)
        self.assertEqual(feed, [102, 101])

    def test_follow_unfollow(self):
        self.twitter.postTweet(1, 101)
        self.twitter.postTweet(2, 102)
        self.twitter.follow(1, 2)
        feed = self.twitter.getNewsFeed(1)
        self.assertEqual(feed, [102, 101])
        self.twitter.unfollow(1, 2)
        feed = self.twitter.getNewsFeed(1)
        self.assertEqual(feed, [101])


if __name__ == '__main__':
    unittest.main()
