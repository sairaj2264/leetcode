class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        answer = 0

        for i in range(0, len(nums)):
            temp = 0
            maxx = nums[i]
            minn = nums[i]
            for j in range (i, len(nums)):
                maxx = max ( maxx, nums[j])
                minn = min (minn, nums[j])
                temp = maxx - minn
                answer = answer + temp
        return answer