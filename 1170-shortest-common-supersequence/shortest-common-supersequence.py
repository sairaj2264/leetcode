class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        dp = [[0] * (len(str2)+1) for _ in range (len(str1)+1)]

        supersequence = []
        for i in range (len(str1)-1,-1,-1):
            for j in range(len(str2)-1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        answer = []
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                answer.append(str1[i])
                i += 1
                j += 1
            else:
                if dp[i][j+1] >= dp[i+1][j]:
                    answer.append(str2[j])
                    j+=1
                else:
                    answer.append(str1[i])
                    i += 1

        while i < len(str1):
            answer.append(str1[i])
            i+=1

        while j < len(str2):
            answer.append(str2[j])
            j+=1

        string = ''.join(answer)
        return string



        # for i in range(len(dp)):
            # print(dp[i])
        # def recurse(i,j):

        #     if i >= len(str1) or j >= len(str2):
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     if str1[i] == str2[j]:
        #         dp[i][j] = 1 + recurse(i+1, j+1)
        #         return dp[i][j]
        #     dp[i][j] = max(recurse(i+1, j), recurse(i, j+1))
        #     return dp[i][j]

        # return recurse(0,0)