class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        dp = [[-1]*3 for _ in range(len(prices) + 2)]
        def recurse(i, status):
            if i >= len(prices):
                return 0

            if dp[i][status] != -1:
                return dp[i][status]
            if status == 0:
                profit_1 = recurse(i+1, status + 1) - prices[i]
                profit_2 = recurse(i+1, status)
                dp[i][status] = max(profit_1, profit_2)
                return dp[i][status]

            
            elif status == 1:
                profit_1 = prices[i] + recurse(i+1,status - 1)
                profit_2 = recurse(i+1, status)
                dp[i][status] = max(profit_1, profit_2)
                return dp[i][status]

        return recurse(0,0)