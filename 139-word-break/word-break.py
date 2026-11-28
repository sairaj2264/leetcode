class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        
        def check(i,j):
            arr = []
            for k in range(i , j + 1):
                arr.append(s[k])
            arr = ''.join(arr)
            if arr in wordDict:
                return True
            return False
        dp = [[-1] * (len(s) + 1) for _ in range(len(s) + 1)]
        def recurse(i,j):
            if j >= len(s) and i >= len(s):
                return True
            
            if j >= len(s):
                return False
            
            if i >= len(s):
                return False
            
            if dp[i][j] != -1:
                return dp[i][j]
            ans = check(i,j)
            if ans == True:
                temp1 = recurse(j+1,j+1)
                temp2 = recurse(i, j+1)
                dp[i][j] = max(temp1, temp2)
                return dp[i][j]
            else:
                dp[i][j] = recurse(i, j+1)
                return dp[i][j]

        return recurse(0,0)

            
        # def recurse(i, arr):

        #     if i > len(wordDict):
        #         return False
        #     temp = ''
        #     if len(arr) > 0:
        #         temp = ''.join(arr)
        #     if temp == s:
        #         return True

        #     a = recurse(i, arr.append(wordDict[i]))
        #     arr.pop()
        #     b = recurse(i+1, arr)
            
        #     if a == True or b == True:
        #         return True
            
        #     return False

        # arr = []
        # return recurse(0 , arr)
        