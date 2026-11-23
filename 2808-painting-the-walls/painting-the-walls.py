class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        
        total = len(time)
        dp = [[-1] * (total + 1) for _ in range(total+1)]
        def recurse(i,covered):

            if covered >= total:
                return 0
            
            if i >= total:
                return float('inf')
            
            if dp[i][covered] != -1:
                return dp[i][covered]
            a = cost[i] + recurse(i+1, covered + 1 + time[i])
            b = recurse(i+1, covered)
            dp[i][covered] =  min(a,b)
            return dp[i][covered]

        return recurse(0,0)