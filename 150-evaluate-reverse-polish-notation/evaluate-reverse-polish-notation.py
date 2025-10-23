class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        n = len(tokens)

        for i in range(n):

            element = tokens[i]

            if not (element == '+' or element == '-' or element == '*' or element =='/'):

                stack.append(int(element))


            else:
                temp1 = stack.pop()
                temp2 = stack.pop()
                ans = 0

                if element == '+':
                    ans = temp1 + temp2
    

                elif element == '-':
                    ans = temp2 - temp1
                
                elif element == '*':
                    ans = temp1 * temp2
                
                else:

                    ans = math.trunc(temp2/temp1)

                stack.append(int(ans))


        answer = stack[-1]
        return(answer)






        