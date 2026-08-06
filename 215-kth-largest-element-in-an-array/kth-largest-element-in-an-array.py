class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        import heapq

        heap = []

        for i in range(0 , len(nums)):
            heapq.heappush(heap, -nums[i])

        element = 0
        for i in range(0 , k):
            element = -heapq.heappop(heap)

        return element

        