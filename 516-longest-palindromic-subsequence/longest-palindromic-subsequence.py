class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        # i = 0
        # j = len(s) - 1
        if len(s) == 1:
            return 1
        
        dp = [[0] * (len(s) + 1) for _ in range(len(s)+1)]

        # i = len(s) - 1
        # j = len(s) -1

        for i in range (len(s) - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = (2 + dp[i+1][j-1])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        n = len(s)- 1
        return dp[0][n]

        # def recurse(i,j):
        #     if i > j:
        #         return 0

        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     if s[i] == s[j]:
        #         if i != j:
        #             dp[i][j] = (2 + recurse(i+1, j-1))
        #         else:
        #             dp[i][j] = (1 + recurse(i+1, j-1))
        #         return dp[i][j]
        #     else:
        #         dp[i][j] = max(recurse(i+1, j), recurse(i, j-1))
        #         return dp[i][j]
        # return recurse(i,j)
        