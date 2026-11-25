class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        i = 0
        j = len(s) - 1
        if len(s) == 1:
            return 1
        
        dp = [[-1] * (len(s) + 2) for _ in range(len(s)+2)]
        def recurse(i,j):
            if i > j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == s[j]:
                if i != j:
                    dp[i][j] = (2 + recurse(i+1, j-1))
                else:
                    dp[i][j] = (1 + recurse(i+1, j-1))
                return dp[i][j]
            else:
                dp[i][j] = max(recurse(i+1, j), recurse(i, j-1))
                return dp[i][j]
        return recurse(i,j)
        