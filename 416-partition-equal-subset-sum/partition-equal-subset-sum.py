class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        summ = 0

        for i in range(0 , len(nums)):
            summ = summ + nums[i]

        if summ%2 == 1:
            return False

        target = summ//2

        
        dp = [[-1] * (target + 1) for i in range(201)]
        def recurse(nums, target, n):



            if n == len(nums):
                return False

            

            if target == 0:
                dp[n][target] = 1
                return True

            if dp[n][target] != -1:
                if dp[n][target] == 1:
                    return True
                return False

            if recurse(nums, target - nums[n], n+1) == True:
                dp[n][target] = 1
                return True
            
            if recurse(nums, target, n+1) == True:
                dp[n][target] = 1
                return True

            dp[n][target] = 0
            return False

        return recurse(nums, target,0)

        