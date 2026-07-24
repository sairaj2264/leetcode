class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        bucket1 = 0
        bucket2 = 0

        for i in range (0 , len(nums)):
            bucket1 = (bucket1 ^ nums[i]) &~(bucket2)
            bucket2 = (bucket2 ^ nums[i]) &~(bucket1)
        
        return bucket1
        