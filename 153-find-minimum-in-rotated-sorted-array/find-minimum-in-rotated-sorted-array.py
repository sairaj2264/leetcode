class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums) - 1

        while (low <= high):
            mid = (low + high)//2

            if nums[low] <= nums[mid]:
                if nums[mid] <= nums[high]:
                    return nums[low]
                else:
                    if nums[mid] < nums[mid + 1]:
                        low = mid
                    else:
                        low = mid + 1
            else:
                if nums[mid] < nums[mid + 1]:
                    high = mid
                else:
                    high = mid + 1

        
