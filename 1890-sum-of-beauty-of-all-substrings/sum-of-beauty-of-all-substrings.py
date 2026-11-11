class Solution:
    def beautySum(self, s: str) -> int:
        
        summ = 0
        for i in range(0 ,len(s)):
            arr = [0]*27
            for j in range(i, len(s)):
                idx = ord(s[j]) - ord('a')
                arr[idx] += 1
                low = 1000
                high = 0
                for k in arr:
                    if k ==0 :
                        continue
                    low = min(low,k)
                    high = max(high,k)
                
                temp = high - low
                summ += temp

        return summ

        