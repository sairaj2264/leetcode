class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        
        dp = [[-1] * 5001 for _ in range(301)]
        def recurse(i, summ):
            if summ > amount:
                return 0
            if i >= len(coins):
                return 0
            
            if summ == amount:
                return 1
            if dp[i][summ] != -1:
                return dp[i][summ]

            total1 = recurse(i,summ + coins[i])
            # total2 = recurse(i+1, summ + coins[i])
            total3 = recurse(i+1, summ)
            dp[i][summ] = total1 + total3
            return dp[i][summ]
        
        return recurse(0,0)

            
            

