class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        dp = [[100000] * (n) for _ in range(m)]

        def clear_dp():
            dp = [[100000] * (n) for _ in range(m)]

        def recurse(i,j):
            if i >= m:
                return 0

            if dp[i][j] != 100000:
                return dp[i][j]
            temp = float('inf')
            minn = j - 1
            if minn < 0:
                minn = 0

            maxx = j + 1

            if maxx >= n:
                maxx = n - 1
            for k in range(minn, maxx+1):
                temp1 = matrix[i][k] + recurse(i+1,k)
                temp = min(temp,temp1)
            dp[i][j] = temp
            return temp
        answer = float('inf')
        for i in range(0, n):
            # clear_dp()
            temp = recurse(0,i)
            answer = min(temp, answer)

        return answer
        