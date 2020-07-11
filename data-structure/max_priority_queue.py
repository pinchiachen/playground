class MaxPriorityQueue:    
    def __init__(self, arr = []):
        self.heap = [None]
        if len(arr) > 0:
            for item in arr:
                self.insert(item)
        self.length = len(self.heap) - 1
        return

    def insert(self, item):
        self.heap.append(item)
        self.length += 1
        self.__swim(self.length)
        return

    def extract_max_item(self):
        self.__swap(1, -1)
        max_item = self.heap.pop()
        self.length -= 1
        self.__sink(1)
        return max_item

    def heap_sort(self, arr):
        sorted_arr = []
        for item in arr:
            self.insert(item)
        while self.length > 0:
            sorted_arr.append(self.extract_max_item())
        return sorted_arr
    
    def __swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        return

    def __swim(self, index):
        while (index > 1) and (self.heap[index] > self.heap[index // 2]):
            self.__swap(index, index // 2)
            index = index // 2
        return

    def __sink(self, index):
        while index * 2 <= self.length:
            max_child_index = self.heap.index(max(self.heap[index * 2], self.heap[index * 2 + 1]))\
                if (index * 2 + 1 <= self.length) else (index * 2)
            if self.heap[index] >= self.heap[max_child_index]:
                break
            self.__swap(index, max_child_index)
            index = max_child_index
        return

def main():
    pq = MaxPriorityQueue([])
    # pq.insert(1)
    # pq.insert(3)
    # pq.insert(2)
    # pq.insert(6)
    # pq.insert(5)
    # print(pq.heap)
    # print(pq.extract_max_item())
    # print(pq.heap)
    print(pq.heap_sort([9, 4, 1, 3, 10, 5, 2, 8, 6, 7]))

if __name__ == "__main__":
    main()
