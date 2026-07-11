class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1
        answer = 0
        if high == 0:
            return nums[0]
        while (low <= high):
            mid = (low + high)//2
            print(mid)
            if nums[low] != nums[low + 1]:
                return nums[low]
            elif nums[high] != nums[high -1]:
                return nums[high]
            
            if nums[mid + 1] != nums[mid]:
                if nums[mid] != nums[mid - 1]:
                    answer = nums[mid]
                    break
                
                elif mid%2 == 0:
                    if nums[mid] == nums[mid - 1]:
                        high = mid
                    else:
                        high = mid - 1

                else:
                    low = mid + 1

            elif nums[mid - 1] != nums[mid]:
                if nums[mid] != nums[mid + 1]:
                    answer = nums[mid]
                    break
                
                elif mid%2 == 0:
                    if nums[mid] == nums[mid + 1]:
                        low = mid
                    else:
                        low = mid + 1

                else:
                    high = mid - 1

        return answer

            

        