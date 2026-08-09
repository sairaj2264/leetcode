class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [-1] * len(nums)
        def recurse(nums, index):

            if index >= len(nums):
                return 0

            if dp[index] != -1:
                return dp[index]
            pick = nums[index] + recurse(nums, index + 2)
            no_pick = recurse(nums,index + 1)

            ans = max(pick, no_pick)
            dp[index] = ans
            return ans
        
        return recurse(nums, 0)