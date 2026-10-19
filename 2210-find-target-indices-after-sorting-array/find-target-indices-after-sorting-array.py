class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:

        answer = []
        nums.sort()
        for i in range (0 , len(nums)):
            if nums[i] == target:
                answer.append(i)
        
        return answer
        