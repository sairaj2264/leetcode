class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        target = sum(stones)//2
        dp = [[-1] * (target +2) for _ in range(len(stones)+2)]
        def recurse(i,summ):
            if i >= len(stones) and summ <= target:
                dp[i][summ] = summ
                return summ

            elif i >= len(stones) or summ > target:
                return -100000

            if dp[i][summ] != -1:
                return dp[i][summ]
            a = recurse(i+1, summ + stones[i])
            b = recurse(i+1, summ)
            dp[i][summ] = max(a,b)
            return max(a,b )

        val = recurse(0,0)
        ans = sum(stones) - (2*val)
        return ans




        # summ = sum(stones)
        # half = summ//2
        # dp = [[-1] * (half + 1) for _ in range(len(stones) + 1)] 
        # def recurse(i, total, target):
        #     if i >= len(stones) or total > target:
        #         return False

        #     if total == target:
        #         return True
        #     if dp[i][total] != -1:
        #         return dp[i][total]

            
        #     ans1 = recurse(i+1, total + stones[i], target)
        #     ans2 = recurse(i+1, total, target)
        #     if ans1 == True or ans2 == True:
        #         dp[i][total] = True
        #         return True
        #     dp[i][total] = False
        #     return False
        # i = half
        # while i >= 0:
        #     ans = recurse(0,0 , i)
        #     if ans == True:
        #         i = ans
        #         break
        #     i -= 1
        # return abs((summ - half) - ans)

        