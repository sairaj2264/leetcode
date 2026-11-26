class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        

        dp = [[-1] * 501 for _ in range(501)]
        def recurse(i,j):
            
            if i >= len(word1):
                return (len(word2) - j)
            if j >= len(word2):
                return (len(word1) - i)
            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = recurse(i+1, j+1)
                return dp[i][j]

            else:
                a = 1 + recurse(i+1, j)
                b = 1 + recurse(i, j+1)
                c = 1 + recurse(i+1, j+1)
                dp[i][j] =  min(a,b,c)
                return dp[i][j]
        return recurse(0,0)