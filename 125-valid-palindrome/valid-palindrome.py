class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        n = len(s)
        p2  = n-1
        flag = True
        while(p1 < p2 and flag == True):
            char1 = s[p1]
            char = ''
            if 'A' <= char1 <= 'Z':
                char = chr(ord(char1) + 32)
            elif 'a' <= char1 <= 'z' or '0' <= char1 <= '9':
                char = char1
            else:
                p1+=1
                continue



            charr = ''
            char2 = s[p2]
            if 'A' <= char2 <= 'Z':
                charr = chr(ord(char2) + 32)
            elif 'a' <= char2 <= 'z' or '0' <= char2 <= '9':
                charr = char2
            else:
                p2-=1
                continue

            if char != charr:
                flag = False
                break
            p1+=1
            p2-=1

        if flag == True:
            return True

        return False

        