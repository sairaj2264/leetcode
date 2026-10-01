class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        nse = []
        pse = []

        stack = []

        for i in range(len(heights)):
            if len(stack) == 0:
                stack.append(i)
                pse.append(-1)
            else:
                while(len(stack) > 0):
                    element = stack.pop()
                    if heights[element] < heights[i]:
                        pse.append(element)
                        stack.append(element)
                        break
                    
                if len(stack) == 0:
                    pse.append(-1)
                stack.append(i) 


        stack = []
        for i in range (len(heights) - 1, -1, -1):
            if len(stack) == 0:
                nse.append(len(heights))
                stack.append(i)
            else:
                while(len(stack) > 0):
                    element = stack.pop()
                    if heights[element] < heights[i]:
                        stack.append(element)
                        nse.append(element)
                        break
                if len(stack) == 0:
                    nse.append(len(heights))
                stack.append(i)
                    
        print(pse)
        nse = nse[::-1]
        print(nse)
        maxx = 0

        for i in range(len(nse)):
            temp1 = heights[i] * (nse[i] - pse[i] - 1)
            maxx = max(maxx, temp1)

        return maxx