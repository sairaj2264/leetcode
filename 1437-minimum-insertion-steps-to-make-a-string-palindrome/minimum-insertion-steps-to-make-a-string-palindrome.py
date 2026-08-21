class Solution:
    def minInsertions(self, s: str) -> int:
        
        l1 = len(s) + 1
        l2 = l1
        s1 = s[::-1]
        dp = [[-1] * l2 for _ in range(l1)]
        def recurse(i,j):
            if i < 0 or j < 0:
                return 0

            val1 = 0
            val2 = 0
            val3 = 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == s1[j]:
                val1 = 1 + recurse(i-1, j-1)

            else:
                val2 = recurse(i-1, j)
                val3 = recurse(i, j-1)
            dp[i][j] = max(val1, val2, val3)
            return max(val1, val2, val3)

        
        lis = recurse(len(s) -1, len(s) - 1)

        answer = (len(s)-lis)
        return answer
