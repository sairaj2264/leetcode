class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counter = 0

        total = 0

        for i in range(0 , len(nums)):
            total += nums[i]
        dp = [[-100001]* (len(nums)+ 2) for _ in range(2 * total + 2) ]
        # print(dp)

        def recurse(nums, idx, summ, target):
            if idx >= len(nums):
                if summ == target:
                    return 1
                return 0
            
            if dp[summ][idx] != -100001:
                return dp[summ][idx]
            count1 = recurse(nums, idx + 1, summ + nums[idx], target)
            count2 = recurse(nums, idx + 1, summ - nums[idx], target)
            # count3 = recurse(nums, idx + 1, summ, target)
            dp[summ][idx] = (count1 + count2)
            return (count1 + count2)

        
        ans = recurse(nums, 0, 0, target)
        return ans

            
        