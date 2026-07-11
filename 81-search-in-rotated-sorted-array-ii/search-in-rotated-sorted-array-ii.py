class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        # if nums == [1,0,1,1,1]:
        #     return True

        low = 0
        high = len(nums) - 1
        answer = -1
        while(low<=high):
            mid = (low + high)//2
            if nums[mid] == target:
                answer =  mid
                break

            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1
                high -=1
                continue
            print(mid)

            if nums[low] <= nums[mid]:

                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1
                
                else:
                    low = mid + 1

            else:
                
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                
                else:
                    high = mid - 1

        if answer == -1:
            return False
        else:
            return True