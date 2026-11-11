class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) == 0:
            return ""
        ans = [s[0]]
        ans_len = 1
        def checker (l,r,s):
            nonlocal ans_len
            while(l>= 0 and r < len(s)):
                if s[l] == s[r]:
                    temp = r - l + 1
                    if ans_len < temp:
                        ans.clear()
                        ans_len = temp
                        for i in range(l,r+1):
                            ans.append(s[i])
                    l-=1
                    r +=1
                else:
                    break

        for i in range(0 , len(s)-1):
            checker(i,i,s)
            checker(i,i+1,s)
        final_ans = ''.join(ans)
        return final_ans
        