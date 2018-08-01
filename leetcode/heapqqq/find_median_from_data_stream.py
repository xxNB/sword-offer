class Heap:
    def __init__(self, cmp):
        self.cmp = cmp
        self.heap = [None]

    def __swap__(self, x, y, a):
        a[x], a[y] = a[y], a[x]

    def size(self):
        return len(self.heap) - 1

    def top(self):
        return self.heap[1] if self.size() else None

    def append(self, num):
        self.heap.append(num)
        self.siftUp(self.size())

    def pop(self):
        top, last = self.heap[1], self.heap.pop()
        if self.size():
            self.heap[1] = last
            self.siftDown(1)
        return top

    def siftUp(self, idx):
        while idx > 1 and self.cmp(idx, idx / 2, self.heap):
            self.__swap__(idx / 2, idx, self.heap)
            idx /= 2

    def siftDown(self, idx):
        while idx * 2 <= self.size():
            nidx = idx * 2
            if nidx + 1 <= self.size() and self.cmp(nidx + 1, nidx, self.heap):
                nidx += 1
            if self.cmp(nidx, idx, self.heap):
                self.__swap__(nidx, idx, self.heap)
                idx = nidx
            else:
                break


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.minHeap = Heap(cmp=lambda x, y, a: a[x] < a[y])
        self.maxHeap = Heap(cmp=lambda x, y, a: a[x] > a[y])

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if not self.maxHeap or num > -self.maxHeap.top():
            self.minHeap.append(num)
            if self.minHeap.size() > self.maxHeap.size() + 1:
                self.maxHeap.append(self.minHeap.pop())
        else:
            self.maxHeap.append( -num)
            if self.maxHeap.size() > self.minHeap.size():
                self.minHeap.append(self.maxHeap.pop())

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.minHeap.size() < self.maxHeap.size():
            return self.maxHeap.top()
        else:
            return (self.minHeap.top() + self.maxHeap.top()) / 2.0


c = MedianFinder()
c.addNum(1)
c.addNum(2)
c.findMedian()