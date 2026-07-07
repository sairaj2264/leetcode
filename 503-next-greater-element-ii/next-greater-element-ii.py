class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = deque()
        hm = {}
        for l in range (0,2):
            for i in range (len(nums) - 1, -1, -1):
                if len(stack) == 0:
                    stack.append(nums[i])
                    hm[i] = -1
                elif nums[i] < stack[-1]:
                    hm[i] = stack[-1]
                    stack.append(nums[i])
                elif nums[i] >= stack[-1]:
                    while (len(stack)>0 and nums[i] >= stack[-1]  ):
                        stack.pop()
                    if len(stack) == 0:
                        hm[i] = -1
                        stack.append(nums[i])
                    else:
                        hm[i] = stack[-1]
                        stack.append(nums[i])
                # print(stack)
        
        answer = []
        for i in range(0, len(hm)):
            answer.append(hm[i])
        return answer