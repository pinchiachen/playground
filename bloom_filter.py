import hashlib

class BloomFilter:
    def __init__(self, size = 1000):
        self.size = size
        self.arr = [False] * size
        self.hash_funcs = [
            hashlib.sha384,
            hashlib.sha256,
            hashlib.sha224,
            hashlib.sha1,
            hashlib.md5,
            ]
        return
    
    def add_data(self, data):
        data = data.encode('utf-8')
        for hash_func in self.hash_funcs:
            index = int(hash_func(data).hexdigest(), 16) % self.size
            self.arr[index] = True
        return

    def check_exist(self, data):
        data = data.encode('utf-8')
        for hash_func in self.hash_funcs:
            index = int(hash_func(data).hexdigest(), 16) % self.size
            if not self.arr[index]:
                return False
        return True