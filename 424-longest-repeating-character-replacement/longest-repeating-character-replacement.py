class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hm = {}


        l = 0
        r = 0
        n = len(s)
        max_length = 0
        max_freq = 0

        while(r < n):
            hm[s[r]] = hm.get(s[r],0) + 1
            max_freq = max(max_freq, hm[s[r]])
            length = r - l + 1
            temp = length - max_freq
            if temp <= k:
                max_length = max(max_length,length)
            else:
                hm[s[l]] -= 1
                l+=1
            
            r += 1
        print(hm)
        return max_length
        
        