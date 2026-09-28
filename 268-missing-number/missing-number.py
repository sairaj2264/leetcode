class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        maxx = 0
        minn = 1000000
        for i in nums:
            maxx = max(maxx, i)
            minn = min(minn, i)
        xorr1 = -1
        xorr2 = -1
        for i in range(0 , maxx + 1):
            xorr1 = xorr1 ^ i

        
        for i in nums:
            xorr2 = xorr2 ^ i

        answer = xorr1 ^ xorr2

        if answer == 0 and minn > 0:
            return 0
        elif answer == 0:
            return maxx + 1
        else:
            return answer

        