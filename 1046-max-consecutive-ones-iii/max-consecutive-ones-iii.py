class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        from collections import deque

        q = deque()

        distance = 0
        j = 0

        if k == 0:
            temp = 0
            for i in range(0 , len(nums)):
                if nums[i] == 1:
                    temp += 1
                else:
                    temp = 0
                
                distance = max(distance, temp)
        
        else:
                
            for i in range(0 , len(nums)):
                if nums[i] == 0 and k > 0:
                    k -= 1
                    q.append(i)
                elif nums[i] == 0 and k <= 0:
                    
                    idx = q.popleft()
                    j = idx + 1
                    q.append(i)
                
                temp = i - j + 1
                distance = max(distance, temp)

        return distance

