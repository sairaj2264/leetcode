class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxx = float('-inf')
        summ = 0
        for i in nums:
            summ += i
            if summ < 0:
                maxx = max(maxx, summ)
                summ = 0
                continue

            maxx = max(maxx, summ)
        # if maxx == 0:
        #     return -1

        return maxx
