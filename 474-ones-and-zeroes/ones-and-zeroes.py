class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        
        dp = [[[-1] * (n+2) for _ in range(m+2)]for _ in range(len(strs)+2)]

        def recurse(i,j,k):
            if i == len(strs) and j <= m and k <= n:
                return 0

            if i > len(strs) or j > m or k > n:
                return float('-inf')

            temp0 = 0
            temp1 = 0
            for z in strs[i]:
                if z == '0':
                    temp0 += 1
                else:
                    temp1 += 1
            if dp[i][j][k] != -1:
                return dp[i][j][k]
            temp2 = 1 + recurse(i+1, j+temp0, k+temp1)
            temp3 = recurse(i+1, j,k)

            dp[i][j][k] = max(temp2, temp3)
            return dp[i][j][k]

        return recurse(0,0,0)


