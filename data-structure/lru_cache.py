class TreeNode():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self
        self.next = self

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.hash_table = dict()
        self.root = TreeNode(0, 0)

    def get(self, key):
        if key not in self.hash_table: return -1
        node = self.hash_table[key]
        self.__removeFromList(node)
        self.__insertIntoHead(node)
        return node.value

    def put(self, key, value):
        if key in self.hash_table:
            node = self.hash_table[key]
            self.__removeFromList(node)
            self.__insertIntoHead(node)
            node.value = value
        else:
            if self.size == self.capacity:
                self.__removeFromTail()
                self.size -= 1
            node = TreeNode(key, value)
            self.__insertIntoHead(node)
            self.hash_table[key] = node
            self.size += 1
        return

    def __removeFromList(self, node):
        if node == self.root: return
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node
        node.next = None
        node.prev = None

    def __insertIntoHead(self, node):
        head_node = self.root.next
        head_node.prev = node
        self.root.next = node
        node.prev = self.root
        node.next = head_node

    def __removeFromTail(self):
        if self.size == 0: return
        tail_node = self.root.prev
        self.__removeFromList(tail_node)
        self.hash_table.pop(tail_node.key, None)

def main():
    lru_cache = LRUCache(3)
    lru_cache.put('apple', 2)
    print(lru_cache.get('apple'))
    lru_cache.put('banana', 4)
    print(lru_cache.get('banana'))
    lru_cache.put('orange', 7)
    print(lru_cache.get('orange'))
    lru_cache.put('grape', 5)
    print(lru_cache.get('apple'))
    print(lru_cache.get('grape'))
    lru_cache.put('grape', 9)
    print(lru_cache.get('grape'))

if __name__ == "__main__":
    main()