class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        dp = [[-1] * 5 for _ in range(len(prices)+2)]
        def recurse(i,state):
            j = state

            if i >= len(prices) or state > 3:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            if state == 0:
                profit_1 = recurse(i+1, 1) - prices[i]
                profit_2 = recurse(i+1, 0)
                dp[i][j] = max(profit_1, profit_2)
                return dp[i][j]

            elif state == 1:
                profit_1 = prices[i] + recurse(i+1, 2)
                profit_2 = recurse(i+1, 1)
                dp[i][j] = max(profit_1, profit_2)
                return dp[i][j]

            elif state == 2:
                profit_1 = recurse(i+1,3) - prices[i]
                profit_2 = recurse(i+1, 2)
                dp[i][j] = max(profit_1, profit_2)
                return dp[i][j]

            elif state == 3:
                profit_1 = recurse(i+1, 3)
                profit_2 = prices[i] + recurse(i+1, 4)
                dp[i][j] = max(profit_1, profit_2)
                return dp[i][j]
        return recurse(0,0)