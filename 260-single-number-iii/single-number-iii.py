class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        

        if len(nums) == 2:
            return nums

        value = 0
        for i in range (0, len(nums)):
            value ^= nums[i]

        
        minNumber = (value & (value - 1))^value

        bucket1 = 0
        bucket2 = 0

        for i in range (0, len(nums)):
            if nums[i] & minNumber > 0:
                bucket1 ^= nums[i]
            else:
                bucket2 ^= nums[i]

        return [bucket1, bucket2]
