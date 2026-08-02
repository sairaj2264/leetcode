class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        from collections import deque
        q = deque()
        n = len(board)
        m = len(board[0])
        visited = [[0] * m for _ in range(n)]

        print(visited)

        def dfs(visited,x,y):
            for i in range(-1, 2):

                for j in range (-1, 2):

                    if abs(i + j) == 1:

                        a = x + i
                        b = y + j

                        n = len(visited)
                        m = len(visited[0])
                        if a>= 0 and a < n and b >= 0 and b < m:
                            if board[a][b] == "O" and visited[a][b] == 0:
                                visited[a][b] = 1
                                dfs(visited,a,b)

        for i in range(0, n):
            if visited[i][0] == 0 and board[i][0] == "O":
                visited[i][0] = 1
                dfs(visited,i,0)


        for i in range(0, m):
            if visited[0][i] == 0 and board[0][i] == "O":
                visited[0][i] = 1
                dfs(visited,0,i)

        for i in range(0, m):
            if visited[n-1][i] == 0 and board[n-1][i] == "O":
                visited[n-1][i] = 1
                dfs(visited,n-1,i)

        for i in range(0, n):
            if visited[i][m-1] == 0 and board[i][m-1] == "O":
                visited[i][m-1] = 1
                dfs(visited,i,m-1)

        for i in range (0 , n):

            for j in range (0 , m):
                if visited[i][j] == 1:
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"


        # stack = []
        # q = deque()
        # m = len(board[0])
        # n = len(board)
        # visited = [[1] * m for _ in range(n)]

        # for i in range (0 , n):
            
            
        #     for j in range ( 0 ,m):

        #         if board[i][j] == "X":
        #             visited[i][j] = 1
        #         else:
        #             visited[i][j] = 0
        #             q.append((i,j))

        # # print(visited)

        # while (len(q) > 0):
        #     element = q.popleft()
        #     x = element[0]
        #     y = element[1]
        #     cnt = 0
        #     count = 0
        #     for i in range (-1, 2):

        #         for j in range (-1, 2):

        #             if abs(i + j) == 1:
        #                 x = i + element[0]
        #                 y = j + element[1]

        #                 if x > 0 and x < (n-1) and y > 0 and y < (m - 1):
        #                     if visited[x][y] == 1:
        #                         cnt += 1
        #                         count += 1
        #                     elif visited[x][y] == 0:
        #                         cnt += 1

        #     x = element[0]
        #     y = element[1]
        #     if cnt < 4:
        #         visited[x][y] = 0
        #         while (len(stack) > 0):
        #             ele = stack.pop()
        #             x = ele[0]
        #             y = ele[1]
        #             visited[x][y] = -1

        #     elif cnt == 4 and count == 4:
        #         visited[x][y] = 1
        #         while(len(stack) > 0):
        #             ele = stack.pop()
        #             x = ele[0]
        #             y = ele[1]
        #             visited[x][y] = 1


        #     elif cnt == 4:
        #         stack.append((x,y))
        #         visited[x][y] = 1
            
        
        # for i in range (0 , len(board)):
            
            
        #     for j in range ( 0 ,m):

        #         if visited[i][j] == 1:
        #             board[i][j] = "X"
        #         else:
        #             board[i][j] = "O"


        # # return board

        


                        
        
                        


