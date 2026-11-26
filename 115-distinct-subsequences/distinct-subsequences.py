class Solution:
    # import sys
    # print(sys.getrecursionlimit())
    def numDistinct(self, s: str, t: str) -> int:
        
        dp = [[-1] * 1001 for _ in range(1001)]

        def recurse(i,j):
            
            if j >= len(t):
                return 1
            elif i >= len(s):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            a = 0
            b = 0
            c = 0
            if s[i] == t[j]:
                a = recurse(i+1, j)
                b = recurse(i+1, j+1)
                dp[i][j] = (a + b)
                return dp[i][j]

            c = recurse(i+1, j)
            dp[i][j] = c

            return dp[i][j]

        return recurse(0,0)