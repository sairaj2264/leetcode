class Solution:
    def checkValidString(self, s: str) -> bool:


        minn = 0
        maxx = 0

        i = 0


        while ( i < len(s)):

            if s[i] == "(":

                minn += 1
                maxx += 1
            
            elif s[i] == ")":
                
                if minn > 0:
                    minn -= 1
                maxx -= 1

                if maxx < 0:
                    return False



            else:
                if minn > 0:
                    minn -= 1
                
                maxx += 1
            
            i+=1

        if minn == 0 or maxx == 0:
            return True

        return False


        

        # cb = 0
        # ob = 0
        # star = 0

        # for i in range (0 , len(s)):
        #     if s[i] == '(':
        #         ob += 1
        #     elif s[i] == ')':
        #         cb += 1
        #     else:
        #         star += 1

        # if (cb + star) >= ob and (ob + star) >= cb:
        #     stack = []
        #     i = 0
        #     if cb == ob:
        #         while (i < len(s)):
        #             if s[i] == "(":
        #                 stack.append("(")
        #             elif s[i] == "*":
        #                 continue
        #             else:
        #                 if s[i] == ")" and stack[-1] == "(":
        #                     stack.pop()
        #                 else:
        #                     return False


        #     if cb > ob:
        #         while (i < len(s)):
        #             if s[i] == "(":
        #                 stack.append("(")
        #             elif s[i] == "*":
        #                 stack.append("(*")
        #             else:
        #                 if s[i] == ")" and stack[-1] == "(":
        #                     stack.pop()
        #                 else:
        #                     return False


        #     if cb == ob:
        #         while (i < len(s)):
        #             if s[i] == "(":
        #                 stack.append("(")
        #             elif s[i] == "*":
        #                 continue
        #             else:
        #                 if s[i] == ")" and stack[-1] == "(":
        #                     stack.pop()
        #                 else:
        #                     return False

        
        # else:
        #     return False

                
        