class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        valid_exclude = []

        pending = 0
        for i in range(len(s)):
            if pending == 0:
                valid_exclude.append(i)
            if s[i] == '(':
                pending += 1
            elif s[i] == ')':
                pending -= 1
            if pending == 0:
                valid_exclude.append(i)

        ans = []
        j = 0
        for i in range(0 , len(s)):
            if i == valid_exclude[j]:
                j += 1
                continue
            ans.append(s[i])

        ans = ''.join(ans)
        return ans
             

