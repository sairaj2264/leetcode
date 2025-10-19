class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        
        for i in range(n):
            flag = False
            for j in range(n):
                if i != j and s[i] == s[j]:
                    flag = True
                    break
            if not flag:
                return i

        return -1


                 
        