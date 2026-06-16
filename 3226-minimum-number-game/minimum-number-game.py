class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        n = len(nums)
        temp = 0
        i = 0
        for i in range (0,n-1, 2):
            temp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = temp
        return nums
