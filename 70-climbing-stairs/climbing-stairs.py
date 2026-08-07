class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [-1] * (n + 1)

        def climb ( count, dp):
            if count <= 3:
                return count
            
            if dp[count] != -1:
                return dp[count]
            a = climb(count - 1, dp)
            b = climb(count - 2, dp)
            dp[count] = (a + b)
            return dp[count]
        
        answer = climb(n, dp)
        return (answer)