class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        dp = [[-1]* (amount + 1) for _ in range(len(coins) + 1)]
        def recurse(i, summ):

            if summ == amount:
                return 0
            
            elif i >= len(coins) or summ > amount:
                return 1000000

            if dp[i][summ] != -1:
                return dp[i][summ]
            choice_1 = 1 + recurse(i, summ + coins[i])
            choice_2 = 1 + recurse(i+1, summ + coins[i])
            choice_3 = recurse(i+1, summ)
            dp[i][summ] = min(choice_1, choice_2, choice_3)
            return dp[i][summ]
        answer = recurse(0,0)

        if answer == 1000000:
            return -1
        return answer

        # dp = [-1] * (amount + 1)
        # def recurse(current_sum, amount):
        #     if current_sum > amount:
        #         return 1000000
        #     elif current_sum == amount:
        #         return 0
        #     if dp[current_sum] != -1:
        #         return dp[current_sum]
        #     minimum = 1000000
        #     for i in range(0 , len(coins)):
        #         temp1 = 1 + recurse(current_sum + coins[i], amount)
        #         minimum = min(minimum, temp1)
        #     dp[current_sum] = minimum
        #     return minimum


        
        # answer =  recurse(0,amount)
        # if answer == 1000000:
        #     return -1
        # return answer




        

        