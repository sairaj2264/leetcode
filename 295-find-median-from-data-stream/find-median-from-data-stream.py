class MedianFinder:

    import heapq
    def __init__(self):
        self.min_heap = []
        self.max_heap = []


        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, num)

        len_min_heap = len(self.min_heap)
        len_max_heap = len(self.max_heap)

        diff = len_min_heap - len_max_heap

        if diff > 1:
            element = -1 * heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, element)
        if diff == 1 and len(self.max_heap) > 0:
            element1 = self.min_heap[0]
            element2 = self.max_heap[0] * -1
            if element1 < element2:
                element = -1 * heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, element)
                element1 = heapq.heappop(self.max_heap)* -1
                heapq.heappush(self.min_heap, element1)


    def findMedian(self) -> float:
        len_min_heap = len(self.min_heap)
        len_max_heap = len(self.max_heap)
        diff = abs(len_min_heap - len_max_heap)

        if diff == 0:
            element1 = self.max_heap[0] * -1
            ans = (self.min_heap[0] + element1 )/2
        else:
            ans = float(self.min_heap[0])
        return ans

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()