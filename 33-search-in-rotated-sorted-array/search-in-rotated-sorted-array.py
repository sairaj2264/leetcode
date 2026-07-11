class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # break = -1
        # for i in range (1, len(nums)):
        #     if (nums[i] < nums[i-1]):
        #         break = i

        
        # arr = []

        # for i in range (break, len(nums)):
        #     arr.append(nums[i])

        # for i in range (break):
        #     arr.append(nums[i])

        # print(arr)

        low = 0
        high = len(nums) - 1
        answer = -1
        while(low<=high):
            mid = (low + high)//2
            print(mid)
            if nums[mid] == target:
                answer =  mid
                break

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

        return answer 
            