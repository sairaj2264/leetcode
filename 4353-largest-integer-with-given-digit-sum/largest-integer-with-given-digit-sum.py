class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s == 0:
            return 0

        if (n * 9) < s:
            return -1


        ans = ""
        while(n > 0):
            if s >= 9:
                ans += '9'
                s -= 9
            else:
                ans += str(s)
                s = 0
            n -= 1
        return int(ans)


            
            
            
        