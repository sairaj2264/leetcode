class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        pre = [1]*n
        suff = [1]*n
        pre[0] = nums[0]
        suff[n-1] = nums[n-1]

        for i in range (1,n):
            pre[i] = pre[i-1]*nums[i]

        for i in range(n-2,-1,-1):
            suff[i] = suff[i+1]*nums[i]

        ans = [0]*n
        ans[0] = suff[1]
        ans[n-1] = pre[n-2]
        for i in range (1,n-1):
            ans[i] = pre[i-1] * suff[i+1]

        return ans
