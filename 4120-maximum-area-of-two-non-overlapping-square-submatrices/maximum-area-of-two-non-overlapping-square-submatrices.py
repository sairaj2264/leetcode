class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:

        n = len(mat)
        m = len(mat[0])
        dp = [[0]*(m + 1) for i in range(n + 1)]
        
        count = 0
        if n == 1:
            for i in range(0 , m):
                if mat[0][i] == 1:
                    count += 1


            if count >= 2:
                return 1
            else:
                return 0

        count = 0
        if m == 1:
            for j in range(0 , n):
                if mat[j][0] == 1:
                    count += 1
            if count >= 2:
                return 1
            else:
                return 0



        def findAnswer(k):
            # print(k)
            ans = []
            for i in range(0 , len(dp)):
                for j in range(0 , len(dp[0])):

                    if dp[i][j] == k:
                        ans.append((i,j))
            # print(ans)
            n = len(ans)
            if n < 2:
                return False

            # print(abs(x1 - x2) )
            # print (abs(y1 - y2))
            for x in range(len(ans)):
                for y in range(x + 1, len(ans)):

                    x1, y1 = ans[x]
                    x2, y2 = ans[y]

                    if abs(x1 - x2) >= k or abs(y1 - y2) >= k:
                        return True

            return False
            
        
        count = 0
        for i in range(0 , n):

            for j in range(0, m):
                if mat[i][j] == 0:
                    dp[i+1][j+1] = 0

                else:

                    if i == 0 or j == 0:
                        dp[i+1][j+1] = 1

                    else:
                        dp[i+1][j+1] = 1 + min(
                            dp[i][j+1],
                            dp[i+1][j],
                            dp[i][j]
                        )
        print(dp)

        low = 0
        high = len(dp) - 1
        ans = False
        while(low <= high):
            
            mid = (low + high)//2
            # print(mid)

            ans = findAnswer(mid)
            
            if ans == True:
                answer = mid
                low = mid + 1
                # print(answer)
            else:
                high = mid - 1

        temp = answer * answer
        return temp






        # print(visited)
        # def check(x1,y1, x2, y2):
        #     if x1 == x2 and y1 == y2:
        #         return True
        #         visited[x1][x2] = 1

        #     else:

        #         flag = True
        #         for i in range(x1, (x2 + 1)):
        #             for j in range(y1, (y2 + 1)):
        #                 if flag == True and mat[i][j] == 1:
        #                     visited[i][j] = 1
        #                 else:
        #                     flag = False
        #                     break

        #         if flag == False:
        #             for i in range(x1, (x2 + 1)):
        #                 for j in range(y1, (y2 + 1)):
        #                     visited[i][j] = 0


        # a = 0
        # for i in range(0, n):

        #     for j in range(0 ,m):
        #         if mat[i][j] == 1:
                    
        #             ans = check(i,j,i+1,j+1)
        #             if ans == True
        #             a = (j-i)

        
                    
                    
            