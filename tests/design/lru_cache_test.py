import unittest

from problems.design.lru__cache import LRUCache


class LRUCacheTest(unittest.TestCase):

    def test_get_put(self):
        cache = LRUCache(2)

        # Test cache miss
        self.assertEqual(cache.get(1), -1)

        # Test cache put and get
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)

        # Test cache update
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)  # 2 should be evicted
        self.assertEqual(cache.get(3), 3)

        # Test cache eviction
        cache.put(4, 4)
        self.assertEqual(cache.get(1), -1)  # 1 should be evicted
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_lru_order(self):
        cache = LRUCache(2)

        # Add items
        cache.put(1, 1)
        cache.put(2, 2)

        # Access 1 to make it most recently used
        self.assertEqual(cache.get(1), 1)

        # Add another item, which should evict 2
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(3), 3)

    def test_update_existing_key(self):
        cache = LRUCache(2)

        # Add and update item
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 10)

        # Ensure value is updated
        self.assertEqual(cache.get(1), 10)

        # Add another item, which should evict 2 as 1 was updated recently
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(3), 3)

    def test_capacity(self):
        cache = LRUCache(1)

        # Add item and ensure it is accessible
        cache.put(1, 1)
        self.assertEqual(cache.get(1), 1)

        # Add another item, which should evict the first one
        cache.put(2, 2)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)


if __name__ == '__main__':
    unittest.main()
