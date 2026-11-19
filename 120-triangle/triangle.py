class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        

        n = len(triangle)
        dp = [[float('inf')]* n for _ in range(n)]
        def recurse(i,j):
            if i >= n:
                return 0
            if i == 0:
                return (triangle[0][0] + recurse(i+1,j))

            if dp[i][j] != float('inf'):
                return dp[i][j]
            path_sum1 = triangle[i][j] + recurse(i+1,j)
            path_sum2 = triangle[i][j+1] + recurse(i+1, j+1)
            dp[i][j] = min(path_sum1, path_sum2)
            return min(path_sum1, path_sum2)

        return recurse(0,0)