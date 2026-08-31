class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        if len(s1) != len(s2):
            return False
        
        if len(s1) == 0 or len(s2) == 0:
            return False
        dp = {}
        def recurse(a, b):

            if a == b:
                return True

            if len(a) <= 1 or len(b) <= 1:
                return False

            n = len(a)
            flag = False

            if dp.get((a,b), -2) != -2:
                return dp[(a,b)]
            for i in range(1, n):
                if (recurse(a[0:i], b[n-i:n]) == True and recurse(a[i:n], b[0:n-i]) == True) or (recurse(a[0:i], b[0:i]) == True and recurse(a[i:n], b[i:n]) == True):
                    flag = True
                    break
            dp[(a,b)] = flag
            return flag

        answer = recurse(s1, s2)

        return answer