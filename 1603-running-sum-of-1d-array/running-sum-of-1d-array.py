class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        summ = 0

        for i in range(len(nums)):
            nums[i] += summ
            summ = nums[i]

        return nums
        