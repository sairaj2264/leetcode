class Solution:
    def minCut(self, s: str) -> int:

        dp = [-1] * (len(s) + 1)
        dp1 = [[-1] * (len(s) + 2) for _ in range((len(s) + 2))]


        def isPalin(i,j):
            if i >= j:
                return True
            
            if dp1[i][j] != -1:
                return dp1[i][j]

            if s[i] != s[j]:
                dp1[i][j] = False
                return False
            
            dp1[i][j] = isPalin(i+1, j -1)
            return dp1[i][j]


        def recurse(i):

            if i >= len(s):
                return 0
            
            if dp[i] != -1:
                return dp[i]

            if isPalin(i, len(s)-1) == True:
                dp[i] = 0
                return 0
            answer = float('inf')
            for k in range(i,len(s)):
                if isPalin(i,k) == True:
                    answer = min(answer, (1 + recurse(k+1)))
            dp[i] = answer
            return answer
        ans = recurse(0)
        return ans