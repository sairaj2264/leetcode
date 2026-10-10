class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import deque
        q = deque()

        for i in range(1 , len(board)-1):
            if board[i][0] == "O":
                q.append((i,0))
            right_corner = len(board[0]) - 1
            if board[i][(right_corner)] == "O":
                q.append((i,right_corner))
        
        for j in range (0 , len(board[0])):
            right_corner = len(board[0]) - 1
            if board[0][j] == "O":
                q.append((0, j))
            bottom_down = len(board) - 1
            if board[bottom_down][j] == "O":
                q.append((bottom_down, j))
        

        def check(x,y,board,q):
            board[x][y] = "-"
            if x-1 >= 0:
                if board[x-1][y] == "O":
                    board[x-1][y] = "-"
                    q.append((x-1, y))

            if x + 1 < len(board):
                if board[x+1][y] == "O":
                    board[x+1][y] = "-"
                    q.append((x+1, y))

            if y -1 >= 0:
                if board[x][y - 1] == "O":
                    board[x][y - 1] = "-"
                    q.append((x, y - 1))

            if y + 1< len(board[0]):
                if board[x][y + 1] == "O":
                    board[x][y + 1] = "-"
                    q.append((x, y + 1))
            return q
                    

        while (len(q) > 0):
            x,y = q.popleft()
            q = check(x,y,board,q)

        
        for i in range(0 , len(board)):
            for j in range(0 , len(board[0])):

                if board[i][j] == "-":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        
            
