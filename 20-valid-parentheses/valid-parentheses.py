class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        openn = ['(','{','[']




        n = len(s)

        if n %2 != 0:
            return False

        for i in range(n):
            element = s[i]

            if element in openn:
                stack.append(element)
            

            elif element == ')' and len(stack) > 0:
                temp = stack.pop()

                if temp != '(':
                    return False

                
            
            elif element == ']' and len(stack) > 0:
                temp = stack.pop()

                if temp != '[':
                    return False

            elif element == '}' and len(stack) > 0:
                temp = stack.pop()

                if temp != '{':
                    return False
            else:
                return False

        
        if len(stack) == 0:
            return True
        else:
            return False
                    
                    

        