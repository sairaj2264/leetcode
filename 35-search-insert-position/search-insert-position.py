class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        p1 = 0
        p2 = len(nums) - 1

        answer = 0

        if target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        while (p1 <= p2):
            mid = (p1 + p2)//2

            if nums[mid] > target:
                answer = mid 
                p2 = mid - 1

            elif nums[mid] == target:
                answer = mid
                return answer
            
            else:
                answer = mid
                p1 = mid + 1

        if nums[answer] < target:
            return answer + 1
        else:
            return answer
        