class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        def action(i,j) -> None:
            for x in range(m):
                if matrix[i][x] != None:
                    matrix[i][x] = 0

            for x in range(n):
                if matrix[x][j] != None:
                    matrix[x][j] = 0


        for i in range(n):
            for j in range(m):

                if matrix[i][j] == 0:
                    matrix[i][j] = None

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == None:
                    action(i,j)
                    matrix[i][j] = 0
        