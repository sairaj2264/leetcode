class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        n = len(bloomDay)
        if n < (m * k):
            return -1

        def checker(nums, m, k, x):
            counter = 0
            total = 0
            for i in range (len(nums)):
                
                if (nums[i] - x) <= 0:
                    counter +=1
                else:
                    total += (counter)//k
                    counter = 0
            
            total += (counter)//k
            if total >= m:
                return True

            return False


        low = min(bloomDay)
        high = max(bloomDay)
        answer = high
        while (low <= high):
            mid = (low + high)//2

            if checker(bloomDay, m, k , mid) == True:
                if checker(bloomDay, m, k , (mid - 1)) == True:
                    high = mid - 1
                else:
                    answer = mid
                    break
            else:
                low = mid + 1
        
        return answer


        