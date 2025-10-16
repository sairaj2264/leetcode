class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_nums = [0]*n
        r_nums = [0]*n
        total = 0

        l_max = 0
        for i in range(1,n):
            l_max = max(l_max, height[i-1])
            l_nums[i] = l_max


        r_max = 0
        for i in range(n-2,-1,-1):
            r_max = max(r_max, height[i+1])
            r_nums[i] = r_max

        for i in range(0,n):
            a = l_nums[i]
            b = r_nums[i]
            numm = min(a,b)
            temp = numm - height[i]
            if temp > 0:
                total += temp

        return total


        