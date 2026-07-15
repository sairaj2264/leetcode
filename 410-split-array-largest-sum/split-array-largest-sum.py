class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def checker(arr, k, x):
            
            summ = 0
            counter = 1

            for i in range (0, len(arr)):
                if arr[i] > x:
                    return False
                summ += arr[i]

                if summ > x:
                    summ = nums[i]
                    counter +=1
                
            if counter > k:
                return False
            return True
        # print(checker(nums,k, 18))
        
        low = 0
        high = 9999999999
        answer = 0
        while(low <= high):
            mid = (low + high)//2
            if checker(nums, k, mid) == True:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return answer
