class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        
        k = k * 2
        dp = [[-1] * ( k + 1) for _ in range(len(prices)+1)]
        def recurse(i,j):

            if i >= len(prices) or j > k:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
            if j%2 == 1:
                a = recurse(i+1,j+1) - prices[i]
                b = recurse(i+1, j)
                dp[i][j] = max(a,b)
                return dp[i][j]
            else:
                a = prices[i] + recurse(i+1, j+1)
                b = recurse(i+1,j)
                dp[i][j] = max(a,b)
                return dp[i][j]

        return recurse(0,1)

            