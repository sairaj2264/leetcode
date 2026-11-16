class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        from collections import deque
        q = deque()
        temp = k
        i = 0
        j = 0
        max_cons_ones = 0
        current_cons = 0
        while (i < len(nums)):
            if nums[i] == 1:
                current_cons += 1
                max_cons_ones = max(max_cons_ones, current_cons)
            elif nums[i] == 0 and temp > 0:
                temp -= 1
                q.append(i)
                current_cons += 1
                max_cons_ones = max(max_cons_ones, current_cons)
            elif nums[i] == 0 and temp <= 0:
                q.append(i)
                current_cons += 1
                target = q.popleft()
                while j <= target:
                    current_cons -= 1
                    j += 1
            i+=1
        return max_cons_ones
                


