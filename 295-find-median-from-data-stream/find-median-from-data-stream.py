import heapq

class MedianFinder:

    def __init__(self):
        self.small = []   # Max Heap (store negatives)
        self.large = []   # Min Heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # Ensure every element in small <= every element in large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Balance the heaps
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]

        return (-self.small[0] + self.large[0]) / 2.0