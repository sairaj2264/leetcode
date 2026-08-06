class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        import heapq
        heap = []

        for i in range(0 , len(score)):
            heapq.heappush(heap, - score[i])

        # print(heap)
        hm = {}
        counter = 1
        while (len(heap) > 0):
            element = - heapq.heappop(heap)
            if counter == 1:
                hm[element] = "Gold Medal"
            elif counter == 2:
                hm[element] = "Silver Medal"
            elif counter == 3:
                hm[element] = "Bronze Medal"
            else:
                hm[element] = str(counter)
            counter += 1
        
        answer = []

        for i in range(0 , len(score)):
            answer.append(hm[score[i]])

        return(answer)
        