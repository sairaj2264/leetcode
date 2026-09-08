class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        

        n = len(cardPoints)
        print(n)
        summ = 0
        for i in cardPoints:
            summ += i

        if k == n:
            return summ


        i = 0
        j = n - 1

        maxx = 0
        temp = 0
        while(i < k):
            temp += cardPoints[i]
            i+=1
            maxx = max(maxx, temp)

        i -=1        
        while(i > -1):
            temp -= cardPoints[i]
            i-=1
            temp += cardPoints[j]
            j -= 1
            maxx = max(maxx, temp)

        return maxx




        # dp = {}
        # def recurse(i:int, j:int, k: int, summ: int) -> int:
        #     if k == 0:
        #         return summ
            
        #     if (i,j) in dp:
        #         return dp[(i,j)]

        #     temp1 = recurse(i+1,j, k-1, summ + cardPoints[i])
        #     temp2 = recurse(i, j -1, k -1, summ + cardPoints[j])

        #     dp[(i,j)] = max(temp1, temp2)
        #     return max(temp1, temp2)

        # return recurse(0, len(cardPoints) - 1, k, 0)



