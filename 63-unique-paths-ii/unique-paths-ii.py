class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid) - 1
        n = len(obstacleGrid[0]) - 1
        dp = [[-1] * (n+1) for _ in range(m+1)]
        def recurse(i,j):
            if i == m and j == n and obstacleGrid[i][j] != 1:
                return 1
            
            if i > m or j > n:
                return 0
            
            if obstacleGrid[i][j] == 1:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
            path1 = recurse(i+1, j)
            path2 = recurse(i, j+1)
            dp[i][j] = (path1 + path2)
            return path1 + path2

        return recurse(0 ,0)