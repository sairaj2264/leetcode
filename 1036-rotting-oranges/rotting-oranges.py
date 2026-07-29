class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()

        one_count = 0
        visited = [[0] * len(grid[0]) for _ in range (len(grid))]
        for i in range (0 , len(grid)):
            for j in range (0 , len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    one_count += 1

        if one_count == 0:
            return 0

        def recurse(x, y , q, grid, visited):
            # if visited[x][y] == 1:
            #     return
            # if grid[x][y] == 1:
            grid[x][y] = 2
            visited[x][y] = 1
            #     return
            # grid[x][y] = 1


            for dx in range (-1, 2):
                for dy in range (-1, 2):

                    if abs(dx) + abs(dy) == 1 and (dx + x)>= 0 and (dy + y) >= 0 and (dx + x) < len(grid) and (dy + y )< len(grid[0]):
                        xx = x + dx
                        yy = y + dy
                        if grid[xx][yy] == 1 and visited[xx][yy] == 0:
                            visited[xx][yy] = 1
                            q.append((xx,yy))

            
        counter = -1
        while(len(q) > 0):
 

            i = 0
            size = len(q)
            print(grid)
            while (i < size):
                element = q.popleft()
                x = element[0]
                y = element[1]

                recurse(x, y, q, grid, visited)
                i += 1
            counter += 1

        for i in range (0 , len(grid)):

            for j in range (0 , len(grid[0])):

                if grid[i][j] == 1:
                    return -1

        return counter
        