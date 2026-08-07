class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        import heapq
        heap = []
        hm = {}

        if len(hand)%groupSize != 0:
            return False

        for i in range(0 , len(hand)):
            temp = hm.get(hand[i], 0)
            hm[hand[i]] = (temp + 1)
            if temp == 0:
                heapq.heappush(heap, hand[i])

        # print(heap)
        while(len(heap) > 0):
            minn = heapq.heappop(heap)
            heapq.heappush(heap, minn)
            print(minn)

            for i in range(minn, minn + groupSize):
                if hm.get(i , 0) ==  0:
                    return False
                else:
                    hm[i] -= 1
                    if hm[i] == 0 and minn != i:
                        return False
                    elif hm[i] == 0 and minn == i:
                        heapq.heappop(heap)
                        if len(heap) > 0:
                            minn = heapq.heappop(heap)
                            heapq.heappush(heap, minn)

                        
                    
            
        return True
                



            
