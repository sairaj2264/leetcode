class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0]*n

        if n == 0:
            return 0

        if n == 1:
            return 1
        
        if n == 2:
            return 1

        dp = [-1] * (n + 1)

        def recurse(n):
            if n == 2 or n == 1:
                return 1
            elif n <= 0:
                return 0
            
            if dp[n] == -1:
                answer = recurse(n-1) + recurse(n-2) + recurse(n -3)
                dp[n] = answer
            else:
                answer = dp[n]
            return answer

        return recurse(n)
        