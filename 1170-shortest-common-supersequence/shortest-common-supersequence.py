class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        l1 = len(str1) + 1
        l2 = len(str2) + 1

        dp = [[0]*l2 for _ in range(l1)]

        # print(dp)

        for i in range(1, l1):

            for j in range(1, l2):

                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        lcss = []
        i = l1 - 1
        j = l2 - 1
        while(i > 0 and j > 0):
            if str1[i-1] == str2[j-1]:
                lcss.append(str1[i-1])
                i -= 1
                j -= 1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    lcss.append(str1[i-1])

                    i-=1

                else:
                    lcss.append(str2[j-1])

                    j-=1


        while(i >= 1):
            lcss.append(str1[i - 1])
            i-=1

        while(j >= 1):
            lcss.append(str2[j - 1])
            j -= 1

        lcss = lcss[::-1]
        lcss = ''.join(lcss)
        return lcss






        # lcss1 = []
        # lcss2 = []
        
        # len_lcs = len(lcs)
        # j = 0
        # for i in range(0 , len(str1)):
        #     if j >= len_lcs:
        #         lcss1.append(str1[i])
        #         j+=1
        #         continue
        #     elif str1[i] == lcs[j]:
        #         lcss1.append(str1[i])
        #         j+=1
        #         continue
        #     else:
        #         j+=1
        #         continue

        # # j = 0
        # # for i in range(0 , len(str2)):
        # #     if j >= len_lcs:
        # #         lcss1.append(str1[i])
        # #         j+=1
        # #         continue
        # #     elif str1[i] == lcs[j]:
        # #         lcss1.append(str1[i])
        # #         j+=1
        # #         continue
        # #     else:
        # #         j+=1
        # #         continue

        # # print(lcss1)



