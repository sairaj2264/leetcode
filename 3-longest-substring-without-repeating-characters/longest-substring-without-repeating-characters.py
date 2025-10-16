class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        dictt = {}
        ans = 0
        count = 0
        i = 0
        while(i<n):
            a = s[i]
            if a not in dictt:
                dictt[a] = i
                count+=1
                ans = max(ans, count)
                i+=1
            else:
                i = dictt[a]
                dictt.clear()
                count = 0
                i+=1

        return ans
        