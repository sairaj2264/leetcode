class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        dp = [-1] * (amount + 1)
        def recurse(current_sum, amount):
            if current_sum > amount:
                return 1000000
            elif current_sum == amount:
                return 0
            if dp[current_sum] != -1:
                return dp[current_sum]
            minimum = 1000000
            for i in range(0 , len(coins)):
                temp1 = 1 + recurse(current_sum + coins[i], amount)
                minimum = min(minimum, temp1)
            dp[current_sum] = minimum
            return minimum


        
        answer =  recurse(0,amount)
        if answer == 1000000:
            return -1
        return answer




        

        