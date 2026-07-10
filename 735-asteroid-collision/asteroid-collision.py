class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]-0:
        stack = []
        answers = []

        for i in range (len(asteroids) - 1, -1, -1):
            if len(stack) == 0 and asteroids[i] > 0:
                answers.append(asteroids[i])
            elif len(stack) == 0 and asteroids[i] < 0:
                stack.append(asteroids[i])

            elif len(stack) > 0 and asteroids[i] < 0:
                stack.append(asteroids[i])
            elif len(stack) > 0 and asteroids[i] > 0:
                flag = False
                while(len(stack)!= 0):
                    if abs(stack[-1]) > asteroids[i]:
                        break
                    elif abs(stack[-1]) == asteroids[i]:
                        stack.pop()
                        flag = True
                        break
                    else:
                        stack.pop()
                if len(stack) == 0:
                    if flag == False:
                        answers.append(asteroids[i])
        if len(stack) > 0:
            stack = stack[::-1]
            while(len(stack) > 0):
                temp = stack.pop()
                answers.append(temp)
        answers = answers[:: -1]
        return answers

