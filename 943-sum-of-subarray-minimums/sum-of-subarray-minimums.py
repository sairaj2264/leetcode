class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:


        stack = []
        answer = 0
        pse = []
        nse = []
        m = (1000000000 + 7)

        for i in range (0, len(arr)):
            if len(stack) == 0:
                stack.append(i)
                pse.append(-1)
            else:
                if arr[i] < arr[stack[-1]]:

                    while (len(stack) != 0 and arr[i] < arr[stack[-1]]):
                        stack.pop()

                        if(len(stack) > 0):
                            temp = arr[stack[-1]]
                    if len(stack) > 0:
                        pse.append(stack[-1])
                        stack.append(i)
                    else:
                        pse.append(-1)
                        stack.append(i)
                else:
                    pse.append(stack[-1])
                    stack.append(i)

        while(len(stack)>0):
            stack.pop()

        for i in range (len(arr)-1, -1, -1):
            if len(stack) == 0:
                stack.append(i)
                nse.append(len(arr))
            else:

                if arr[i] <=  arr[stack[-1]]:
                    while (len(stack) > 0 and arr[i] <=  arr[stack[-1]]):
                        stack.pop()                
                    
                    if len(stack) > 0:
                        nse.append(stack[-1])
                    else:
                        nse.append(len(arr))
                    stack.append(i)
                else:
                    nse.append(stack[-1])
                    stack.append(i)

        nse = nse[::-1]
        # print(nse)
        answer = 0
        for i in range (len(arr)):
            left = i - pse[i]
            right = nse[i] - i
            answer = (answer + left * right * arr[i]) % m
            # print(answer)

        # for i in 


        return answer



        # n = len(arr)
        # answer = 0
        # temp = []
        # minn = float('inf')
        # # print min
        # def SumFinder(arr, n, counter, temp, minn, answer):

        #     if counter == n:
        #         return answer
            
        #     minn = min(minn, arr[counter])
        #     temp.append(arr[counter])
        #     a = sumFinder(arr, n, counter + 1, temp, minn, answer)
        #     temp.pop()
        #     b = sumFinder( arr, n, counter + 1, temp. minn, answer)
        #     return
        # n = len(arr)
        # answer = 0

        # for i in range (0, n):
        #     for j in range (i, n):
        #         minn = 30001
        #         for k in range (i, j+1):
        #             minn = min(minn, arr[k])
        #         answer += minn
        # return answer
        