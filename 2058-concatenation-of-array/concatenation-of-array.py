class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lengthh = n * 2
        numss = [0] * lengthh

        for i in range(0,n):
            numss[i] = nums[i]
            numss[i + n] = nums[i]

        return numss