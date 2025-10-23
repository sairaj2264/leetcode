class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        n = len(asteroids)
        stack = []
        for i in range(n):
            element = asteroids[i]
            

            if len(stack) == 0 or element >0:
                stack.append(element)



            else:
                temp1 = stack[-1]

                flag = False
                while( len(stack) > 0 ):
                    
                    temp1 = stack[-1]

                    if abs(element) > temp1:
                        if temp1 > 0:
                            stack.pop()
                            flag = True
                        else:
                            flag = True
                            break
                        
                        

                    elif abs(element) == temp1:
                        if element < temp1:
                            stack.pop()
                            flag = False
                            break
                        else:
                            stack.append(element)
                            break

                    else:
                        flag = False
                        break  


                if flag == True:
                    stack.append(element)
                             
                
        return stack



        