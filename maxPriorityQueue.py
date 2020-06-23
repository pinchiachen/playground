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

    def extractMaxItem(self):
        self.__swap(1, -1)
        maxItem = self.heap.pop()
        self.length -= 1
        self.__sink(1)
        return maxItem

    def heapSort(self, arr):
        sortedArr = []
        for item in arr:
            self.insert(item)
        while self.length > 0:
            sortedArr.append(self.extractMaxItem())
        return sortedArr
    
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
            maxChildIndex = self.heap.index(max(self.heap[index * 2], self.heap[index * 2 + 1]))\
                if (index * 2 + 1 <= self.length) else (index * 2)
            if self.heap[index] >= self.heap[maxChildIndex]:
                break
            self.__swap(index, maxChildIndex)
            index = maxChildIndex
        return

def main():
    pq = MaxPriorityQueue([])
    # pq.insert(1)
    # pq.insert(3)
    # pq.insert(2)
    # pq.insert(6)
    # pq.insert(5)
    # print(pq.heap)
    # print(pq.extractMaxItem())
    # print(pq.heap)
    print(pq.heapSort([9, 4, 1, 3, 10, 5, 2, 8, 6, 7]))

if __name__ == "__main__":
    main()
