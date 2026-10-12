
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        from collections import defaultdict, deque
        q = deque()
        adj = defaultdict(list)

        end_x = len(grid) - 1
        end_y = len(grid[0]) - 1

        dp = [[-1] * len(grid[0]) for _ in range(len(grid))]

        distance = 0

        def dfs(i, j, end_x, end_y):

            if i == end_x and j == end_y:
                return grid[i][j]

            if dp[i][j] != -1:
                return dp[i][j]

            new_i = i + 1
            new_j = j + 1

            temp1 = float('inf')
            temp2 = float('inf')

            if new_i <= end_x:
                temp1 = grid[i][j] + dfs(new_i, j, end_x, end_y)

            if new_j <= end_y:
                temp2 = grid[i][j] + dfs(i, new_j, end_x, end_y)

            dp[i][j] = min(temp1, temp2)

            return dp[i][j]

        distance = dfs(0, 0, end_x, end_y)
        return distance
