class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        from collections import deque
        q = deque()
        n = len(grid)
        m = len(grid[0])
        visited = [[0] * m for _ in range(n)]

        # print(visited)
        def check(x, y):
            xx = [0,0,1,-1]
            yy = [1,-1,0,0]

            for i in range(0 , len(xx)):
                new_x = x + xx[i]
                new_y = y + yy[i]

                if new_x >= 0 and new_x< n and new_y >=0 and new_y < m:

                    if grid[new_x][new_y] == 1 and visited[new_x][new_y] == 0:
                        q.append((new_x, new_y))
                        visited[new_x][new_y] = 1

                




        for i in range(0, n):
            if grid[i][0] == 1 and visited[i][0] == 0:
                visited[i][0] = 1
                q.append((i, 0))
        for i in range(0 , m):
            if grid[0][i] == 1 and visited[0][i] == 0:
                visited[0][i] = 1
                q.append((0, i))
        for i in range(0 , n):
            if grid[i][m-1] == 1 and visited[i][m-1] == 0:
                visited[i][m-1] = 1
                q.append((i, m-1))
        for i in range(0 , m):

            if grid[n-1][i] == 1 and visited[n-1][i] == 0:
                visited[n-1][i] = 1
                q.append((n-1, i))

        while (len(q) > 0):
            element = q.popleft()
            x = element[0]
            y = element[1]
            check(x, y)

        counter = 0
        for i in range (0 , n):

            for j in range(0 , m):
            
                if grid[i][j] == 1 and visited[i][j] == 0:
                    counter += 1

        return counter



                