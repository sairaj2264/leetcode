class Solution:
    def validStrings(self, n: int) -> List[str]:

        def generator(i, n, temp, ans):
            if i >= n:
                s = ''.join(map(str, temp))
                ans.append(s)
                return
            if i == 0:
                temp.append(0)
                generator(i+1, n, temp, ans)
                temp.pop()
                temp.append(1)
                generator(i+1, n, temp, ans)
                temp.pop()
            elif i > 0 and len(temp) > 0:
                if temp[i-1] == 0:
                    temp.append(1)
                    generator(i+1, n, temp, ans)
                    temp.pop()
                else:
                    temp.append(0)
                    generator(i+1, n, temp, ans)
                    temp.pop()
                    temp.append(1)
                    generator(i+1, n, temp, ans)
                    temp.pop()

        ans = []
        temp = []
        generator(0,n, temp, ans)
        return ans