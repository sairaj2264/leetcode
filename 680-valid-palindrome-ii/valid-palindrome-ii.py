class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        p1 = 0
        p2 = n-1
        excep = True

        while(p1<p2):
            if s[p1] == s[p2]:
                p1+=1
                p2-=1

                
            elif s[p1] != s[p2] and excep == True:
                excep = False
                if s[p1+1] == s[p2]:
                    temp = s[p1+1:p2+1]
                    temp1 = temp[::-1]
                    if temp == temp1:
                        return True


                if s[p1] == s[p2-1]:
                    temp = s[p1:p2]
                    temp1 = temp[::-1]
                    if temp == temp1:
                        return True


                else:
                    return False

                  
            else:
                return False


        return True
        