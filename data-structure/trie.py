class Trie:
    def __init__(self):
        self.root = {}
        self.end_char = '#'

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_char] = self.end_char
        return

    def find_word(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_char in node

    def find_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

def main():
    trie = Trie()
    trie.insert('apple')
    trie.insert('air')
    print(trie.root)
    print(trie.find_word('air'))
    print(trie.find_word('apple'))
    print(trie.find_prefix('ai'))
    print(trie.find_prefix('pp'))

if __name__ == "__main__":
    main()