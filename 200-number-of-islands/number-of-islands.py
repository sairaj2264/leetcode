class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        from collections import deque
        q = deque()
        n = len(grid)
        m = len(grid[0])

        visited = [[0] * m for _ in range(n)]
        counter = 0
        # print(visited)
        for i in range( 0 , n):

            for j in range(0 , m):

                if grid[i][j] == "1" and visited[i][j] == 0:
                    visited[i][j] = 1
                    q.append((i,j))
                
                    counter += 1
                    while (len(q) > 0):

                        element = q.popleft()
                        x = element[0]
                        y = element[1]
                        
                        xx = [1,-1,0,0]
                        yy = [0, 0, -1, 1]

                        for r in range( 0 , len(xx)):
                            newX = x + xx[r]
                            newY = y + yy[r]

                            if newX >= 0 and newX < n and newY >= 0 and newY < m:
                                if grid[newX][newY] == "1" and visited[newX][newY] == 0:
                                    visited[newX][newY] = 1
                                    q.append((newX, newY))


        return counter

                                

        
