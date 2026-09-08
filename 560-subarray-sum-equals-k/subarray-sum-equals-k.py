class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        hm = {}
        n = len(nums)
        prefix = 0
        answer = 0
        hm[prefix] = hm.get(prefix, 0) + 1
        for i in range (0 , n):
            prefix += nums[i]
            temp = prefix - k
            num = hm.get(temp,0)
            if num > 0:
                answer += num

            hm[prefix] = hm.get(prefix,0) + 1

        return answer

