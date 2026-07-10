class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        nums = list(map(int, num))
        answer = []

        for i in range (0, len(nums)):

            if k == 0:
                if nums[i] > 0:
                    stack.append(nums[i])
                    continue

                elif len(stack) > 0 :
                        stack.append(nums[i])
                        continue
                else:
                    continue

            if len(stack) == 0:

                if nums[i] == 0:
                    continue
                else:
                    stack.append(nums[i])
            
            else:

                if nums[i] < stack[-1]:
                    while (len(stack) > 0 and k > 0 and nums[i] < stack[-1]):
                        stack.pop()
                        k-=1
                    if nums[i] == 0 :
                        if len(stack) > 0:
                            stack.append(nums[i])
                    else:
                        stack.append(nums[i])


                elif nums[i] >= stack[-1]:
                    stack.append(nums[i])

        while (k > 0 and len(stack) > 0):
            stack.pop()
            k -= 1

        if len(stack) == 0:
            return "0"

        else:
            answer = "".join(map(str, stack))
            return answer

                    

        