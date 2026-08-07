class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        dp = [-1] * (n + 1)
        for i in range(0 , n + 1):
            if i<=3:
                dp[i] = i
            else:
                ans = (dp[i-1] + dp[i-2])
                dp[i] = ans

        
        return dp[n]
