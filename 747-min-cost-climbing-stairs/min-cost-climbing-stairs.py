class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [-1] * len(cost)
        def recurse(cost, index):
            if index >= len(cost):
                return 0
            
            if dp[index] != -1:
                return dp[index]

            one_step = cost[index] + recurse(cost, index +1) 
            two_step = cost[index] + recurse (cost, index + 2)

            dp[index] = min(one_step, two_step)
            return dp[index]
           

        return min(recurse(cost, 0),
        recurse(cost, 1))
                