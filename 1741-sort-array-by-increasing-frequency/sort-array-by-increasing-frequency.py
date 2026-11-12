class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        arr = nums
        import heapq
        hm = {}
        heap = []

        for i in range(0 , len(nums)):
            hm[arr[i]] = hm.get(arr[i],0) +1

        for key in hm:
            heapq.heappush(heap, (hm[key], - key))

        answer = []

        while len(heap) > 0:
            freq, element = heapq.heappop(heap)
            element *= -1
            i = 0
            for i in range(freq):
                answer.append(element)
        return answer        