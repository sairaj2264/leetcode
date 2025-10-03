class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = [1]*10
        new_board = []
        for box in board:
            converted = [int(x) if x!= "." else 0 for x in box]
            new_board.append(converted)

        # for box in new_board:
        #     for i in box:
        #         if i == 0:
        #             continue
        #         check[i]-=1
        #     for i in check:
        #         if i != 0 or i != 1:
        #             return False
        #     check = [1]*10

        for j in range(0,3):
            for k in range(0,3):
                l = new_board[j][k]
                if l != 0:
                    check[l]-=1 

        for k in check:
            if k not in (0,1):
                return False
        check = [1]*10









        for j in range(0,3):
            for k in range(3,6):
                l = new_board[j][k]
                if l != 0:
                    check[l]-=1 

        for k in check:
            if k not in (0,1):
                return False
        check = [1]*10




        for j in range(0,3):
            for k in range(6,9):
                l = new_board[j][k]
                if l != 0:
                    check[l]-=1 

        for k in check:
            if k not in (0,1):
                return False
        check = [1]*10





        for j in range(3,6):
            for k in range(0,3):
                l = new_board[j][k]
                if l != 0:
                    check[l]-=1 

        for k in check:
            if k not in (0,1):
                return False
        check = [1]*10







        for j in range(3,6):
            for k in range(3,6):
                l = new_board[j][k]
                if l != 0:
                    check[l]-=1 

        for k in check:
            if k not in (0,1):
                return False
        check = [1]*10




        for j in range(3,6):
            for k in range(6,9):
                l = new_board[j][k]
                if l != 0:
                    check[l]-=1 

        for k in check:
            if k not in (0,1):
                return False
        check = [1]*10


        for j in range(6,9):
            for k in range(0,3):
                l = new_board[j][k]
                if l != 0:
                    check[l]-=1 

        for k in check:
            if k not in (0,1):
                return False
        check = [1]*10



        for j in range(6,9):
            for k in range(3,6):
                l = new_board[j][k]
                if l != 0:
                    check[l]-=1 

        for k in check:
            if k not in (0,1):
                return False
        check = [1]*10



        for j in range(6,9):
            for k in range(6,9):
                l = new_board[j][k]
                if l != 0:
                    check[l]-=1 

        for k in check:
            if k not in (0,1):
                return False
        check = [1]*10


        for i in range (0,9):
            for j in range(0,9):
                k = new_board[i][j]
                if k != 0:
                    check[k]-=1
                     
            
            for k in check:
                if k not in (0,1):
                    return False
            check = [1]*10
        

        for i in range (0,9):
            for j in range(0,9):
                k = new_board[j][i]
                if k != 0:
                    check[k]-=1
                     
            
            for k in check:
                if k not in (0,1):
                    return False
            check = [1]*10

        return True
