class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        hm = {}
        prefix = 0
        n = len(nums)
        hm[0] = 1
        ans = 0
        for i in range(0,n):
            if nums[i] % 2 == 1:
                prefix += 1

            temp = prefix - k
            temp2 = hm.get(temp, 0)
            ans += temp2
            hm[prefix] = hm.get(prefix,0) + 1

        return ans

        