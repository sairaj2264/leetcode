class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [-1] * (n+1)
        def recurse(n):
            if n == 0:
                return 1
            elif n < 0:
                return 0
            
            if dp[n] != -1:
                return dp[n]
            temp1 = 0
            temp2 = 0

            temp1 =  recurse(n - 1)
            temp2 =  recurse(n - 2)
            dp[n] = (temp1 + temp2)
            return (temp1 + temp2)

        return recurse(n)

