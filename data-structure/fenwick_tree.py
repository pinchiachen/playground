class FenwickTree:
    def __init__(self, nums):
        l = len(nums)
        self.sums = [0] * (l + 1)
        for i in range(len(nums)):
            self.update(i+1, nums[i])

    def update(self, idx, delta):
        while idx < len(self.sums):
            self.sums[idx] += delta
            idx += self.__lowbit(idx)

    def query(self, idx):
        total = 0
        while idx > 0:
            total += self.sums[idx]
            idx -= self.__lowbit(idx)
        return total

    def __lowbit(self, val):
        return val & (-val)

def main():
    nums = [1, 2, 3, 4, 5]
    fenwick_tree = FenwickTree(nums)
    print(fenwick_tree.query(3))
    print(fenwick_tree.query(4))
    print(fenwick_tree.query(5))
    fenwick_tree.update(3, 4)
    print(fenwick_tree.query(3))
    print(fenwick_tree.query(4))
    print(fenwick_tree.query(5))

if __name__ == "__main__":
    main()