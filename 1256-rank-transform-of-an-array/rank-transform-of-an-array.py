class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        import heapq
        heap = []
        hm = {}
        answer = []

        for i in range(0 , len(arr)):
            heapq.heappush(heap, arr[i])
        print(heap)        
        i = 1

        while(len(heap) > 0):
            element = heapq.heappop(heap)
            if hm.get(element, 0) == 0:
                hm[element] = i
                i += 1

        # print(hm)

        for i in range(0 , len(arr)):
            answer.append(hm[arr[i]])
        return answer