class Solution:
    def rob(self, nums: list[int]) -> int:

        n = len(nums)
        dp = [0] * (n + 2)

        dp[0] = nums[0]

        for i in range(n-1,-1,-1):
            sum1 = nums[i] + dp[i+2]
            sum2 = dp[i+1]
            dp[i] = max(sum1, sum2)


        return dp[0]

        # def recurse(i):
        #     if i >= n:
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]
        #     sum1 = nums[i] + recurse(i+2)
        #     sum2 = recurse(i+1)
        #     dp[i] = max(sum1, sum2)
        #     return max(sum1, sum2)

        # return recurse(0)
        