class LRUCache:
    def __init__(self, size):
        self.size = size
        self.hash_table = dict()
        self.cache_queue = []

    def get(self, key):
        if key not in self.hash_table: return -1
        self.cache_queue.remove(key)
        self.cache_queue.insert(0, key)
        return self.hash_table[key]

    def put(self, key, value):
        if (key in self.hash_table) or (len(self.cache_queue) > self.size):
            return self.cache_queue
        if len(self.cache_queue) == self.size:
            pop_key = self.cache_queue.pop()
            self.hash_table.pop(pop_key, None)
        self.cache_queue.insert(0, key)
        self.hash_table[key] = value
        return self.cache_queue

def main():
    lru_cache = LRUCache(3)
    print(lru_cache.put('apple', 2))
    print(lru_cache.put('banana', 4))
    print(lru_cache.put('orange', 7))
    print(lru_cache.put('grape', 5))
    print(lru_cache.get('apple'))
    print(lru_cache.get('grape'))
    print(lru_cache.put('grape', 9))

if __name__ == "__main__":
    main()