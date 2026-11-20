class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        from collections import deque

        q = deque()
        answer = []
        i = 0
        while i < k:
            if len(q) == 0:
                q.append(i)
            else:
                element = nums[q[-1]]
                while len(q) > 0 and element < nums[i]:
                    q.pop()
                    if len(q) > 0:
                        element = nums[q[-1]]
                q.append(i)

            i += 1

        j = 0
        i -= 1


        while i < len(nums):
            
            answer.append(nums[q[0]])
            j += 1
            i += 1
            if i >= len(nums):
                break
            idx = q[0]
            if j > idx:
                q.popleft()

            if len(q) > 0:
                element = nums[q[-1]]
                while len(q) > 0 and element < nums[i]:
                    
                    q.pop()
                    if len(q) > 0:
                        element = nums[q[-1]]
            q.append(i)

        return answer
            



        