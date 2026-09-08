class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0


        prefix = 0
        hm = {}
        n = len(nums)
        hm[0] = 1

        for i in range(0,n):
            prefix += nums[i]

            temp = prefix - goal

            temp1 = hm.get(temp,0)
            ans += temp1

            hm[prefix] = hm.get(prefix,0) + 1
        
        return ans

