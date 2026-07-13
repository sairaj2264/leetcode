class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def checker(nums, threshold, x):
            result = 0
            if x == 0:
                return False
            for i in range (len(nums)):
                result += int(ceil(nums[i]/x))
            
            if result <= threshold:
                return True
            return False

        low = 1
        high = max(nums)
        answer = 0
        while(low <= high):
            mid = (low + high)//2

            if checker(nums, threshold, mid) == True:
                if checker(nums, threshold, mid - 1) == True:
                    high = mid - 1
                else:
                    answer = mid
                    break
            else:
                low = mid + 1

        return answer

        