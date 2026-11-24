class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        max_profit = (minProfit + 2)
        max_group = (n + 2)

        dp = [[[-1] * (max_group + 2) for _ in range(max_profit + 2) ]for _ in range(len(group) + 2)]
        def recurse(i,p,count):


            if i == len(group) and p >= minProfit and count <= n:
                return 1

            if i >= len(group):
                return 0


            if dp[i][p][count] != -1:
                return dp[i][p][count]

            new_profit = min(minProfit, p + profit[i])
            new_count = min(n+1, count+group[i])
            dp[i][p][count] = (recurse(i+1, new_profit, new_count) + recurse(i+1, p, count))%1000000007
            return dp[i][p][count]
            
        return recurse(0,0,0)%1000000007

            
        