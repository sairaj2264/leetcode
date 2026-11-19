class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1] * (n +1) for _ in range(m+1)]
        def recurse(i,j):
            if i == m-1 and j == n-1:
                return 1
            elif i > m-1 or j > n - 1:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            one = recurse(i+1,j)
            two = recurse(i, j + 1)
            dp[i][j] = one + two
            return (one+two) 

        
        return recurse(0 , 0)