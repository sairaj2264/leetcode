class Solution:
    def calPoints(self, operations: List[str]) -> int:
    
        stack = []


        for i in operations:
            if i == 'C':
                stack.pop()
            elif i == 'D':
                temp = 2 * stack[-1]
                stack.append(temp)
            elif i == '+':
                temp1 = stack.pop()
                temp2 = stack.pop()
                temp3 = temp1 + temp2
                stack.append(temp2)
                stack.append(temp1)
                stack.append(temp3)
            else:
                stack.append(int(i))


        summ = sum(stack)
        return summ
        