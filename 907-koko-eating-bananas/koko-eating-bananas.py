class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        n = len(piles)
        low = 1
        high = max(piles)
        answer = 0
        if h == n:
            return high

        if n == 1 :
            return int(ceil(piles[0]/h))


        def consume(x):
            temp = 0
            piles2 = piles.copy()
            i = 0
            # and temp < h
            while (i < n ):
                temp += int(ceil(piles2[i]/x))
                i+=1
            return temp


        while (low <= high):

            mid = (low + high)//2


            temp = consume(mid)


            # elif temp == -2:
            #     high = mid - 1

            if temp <= h:
                answer = mid
                high = mid - 1

            elif temp > h:
                low = mid + 1

        
        return answer

        





        