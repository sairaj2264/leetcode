class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[-1] * (len(word2) + 1) for _ in range(len(word1)+1)]
        def recurse(i,j):
            if i >= len(word1) or j >= len(word2):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = 1 + recurse(i+1, j+1)
                return dp[i][j]
            else:
                matching_1 = recurse(i+1, j)
                matching_2 = recurse(i, j+1)
                dp[i][j] = max(matching_1, matching_2)
                return dp[i][j]

        matching = recurse(0,0)
        answer = ((len(word1) - matching) + (len(word2) - matching))
        return answer

        