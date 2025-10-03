class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:

        n = len(matrix)
        check = [1] * n

        for i in range(n):
            for j in range(n):
                value = matrix[i][j] - 1
                check[value] -= 1

            for l in check:
                if l != 0:
                    return False
            check = [1] * n



        

        for i in range(n):
            for j in range(n):
                value = matrix[j][i] - 1
                check[value] -= 1

            for l in check:
                if l != 0:
                    return False
            check = [1] * n


        return True