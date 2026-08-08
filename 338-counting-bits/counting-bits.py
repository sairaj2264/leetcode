class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        elif n ==1:
            return [0,1]
        answer = [-1] * (n + 1)
        answer[0] = 0
        answer[1] = 1
        
        def recurse(n,count,dp, offset):
            # if count == 1:
            #     return 1
            
            # if count == 0:
            #     return 0

            if count > n:
                return
            
            if dp[count] == -1:

                if (offset * 2) == count:
                    offset = count
                    
                dp[count] = dp[count - offset] + 1
                
            recurse(n, count + 1, dp, offset)
        
        recurse(n,1, answer, 2)
        return answer