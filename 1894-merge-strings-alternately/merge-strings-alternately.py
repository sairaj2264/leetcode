class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        p1=0
        p2=0


        n = len(word1)
        m = len(word2)

        ans = ''
        while(p1 < n and p2 < m):
            ans = ans + word1[p1]
            ans = ans + word2[p2]
            p1+=1
            p2+=1

        while(p1 < n):
            ans = ans + word1[p1]
            p1+=1

        while(p2 < m):
            ans = ans + word2[p2]
            p2+=1

        return ans

        