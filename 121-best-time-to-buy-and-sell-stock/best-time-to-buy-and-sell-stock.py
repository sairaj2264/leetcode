class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = 2**31 - 1

        profit = 0

        n = len(prices)

        for i in range(n):
            val = prices[i]
            minn = min(minn,val)
            
            temp = val - minn

            profit = max(temp, profit)


        return profit 
        