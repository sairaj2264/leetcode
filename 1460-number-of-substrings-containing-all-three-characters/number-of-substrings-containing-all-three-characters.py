class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        arr = [-1] * 3
        n = len(s)
        answer = 0
        for i in range(0,n):
            temp = ord(s[i]) - ord('a')
            arr[temp] = i

            flag = True
            minn = float('inf')
            for element in arr:
                if element == -1:
                    flag = False
                    break
                minn = min(minn, element)
            if flag == True:
                answer += minn + 1

        return answer
            
            
        