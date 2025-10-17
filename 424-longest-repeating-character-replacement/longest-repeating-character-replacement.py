class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        lenn = 0
        n = len(s)
        maxSize = 0

        p1= 0
        freq = [0] * 26
        for i in range(n):
            char = s[i]
            key = ord(char) - ord('A')
            freq[key]+=1
            count = 0
            
            maxx = 0
            for j in freq:
                maxx = max(maxx, j)
                if j > 0:
                    count += 1
            
            size = i - p1 + 1
            val = size - maxx
            if val<=k:
                maxSize = max(maxSize, size)
            else:
                ele = s[p1]
                elem = ord(ele) - ord('A') 
                freq[elem]-=1
                p1+=1
                i-=1



        return maxSize



            

        

        



