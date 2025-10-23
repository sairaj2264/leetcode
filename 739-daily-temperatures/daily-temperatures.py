class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        
        stack = []
        n = len(temperatures)
        answer = [0]*n
        last = 0
        
        i = 0
        while(i<n):
            element = temperatures[i]


            if len(stack) == 0:
                stack.append([element,i])


            else:
                if stack[-1][0]<element:
                    temp = i - stack[-1][1]
                    index = stack[-1][1]
                    answer[index] = temp
                    stack.pop()
                    i-=1
                else:
                    stack.append([element,i])
            i+=1

        
        return answer

            





        