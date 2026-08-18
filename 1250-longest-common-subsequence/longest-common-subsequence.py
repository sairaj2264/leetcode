class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[-1] * (len(text2) + 2) for _ in range(len(text1) + 2)]
        def recurse(text1, text2, idx1, idx2):
            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0
            if dp[idx1][idx2] != -1:
                return dp[idx1][idx2]

            if text1[idx1] == text2[idx2]:
                
                temp =  (1 + recurse(text1 , text2 , idx1 + 1, idx2 + 1))
                dp[idx1][idx2] = temp
                return temp

            elif text1[idx1] != text2[idx2]:
                val1 = recurse(text1, text2, idx1 + 1, idx2)
                val2 = recurse(text1, text2, idx1, idx2 + 1)

                temp = max(val1, val2)
                dp[idx1][idx2] = temp
                return temp

        return (recurse(text1, text2, 0, 0))        