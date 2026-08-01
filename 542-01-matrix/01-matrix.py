class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        visited = [[-1] * len(mat[0]) for _ in range (0 , len(mat))]

        # print(visited)
        from collections import deque
        q = deque()

        
        for i in range(0 , len(mat)):
            for j in range (0 , len(mat[0])):
                if mat[i][j] == 0:
                    visited[i][j] = 0
                    q.append((i , j))

        while (len(q) > 0):
            element = q.popleft()
            x = element[0]
            y = element[1]

            xxx = [0, 0, -1, 1]
            yyy = [-1, 1, 0, 0]

            for i in range (0 , 4):
                xx = xxx[i]
                yy = yyy[i]
                if (x + xx) >= 0 and (x + xx) < len(mat) and (yy + y) >= 0 and (yy + y) < len(mat[0]): 
                    if visited[xx + x][yy + y] == -1:
                        visited[xx + x][yy + y] = (visited[x][y] + 1)
                        q.append(((xx + x), (yy + y)))
                
        return visited

