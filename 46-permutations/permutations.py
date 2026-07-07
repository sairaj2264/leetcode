class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        temp = []
        n = len(nums)

        def permuFinder (nums, n, temp, answer, counter):
            for i in range (0,n):
                if nums[i] not in temp:
                    temp.append(nums[i])
                    permuFinder (nums, n, temp, answer, counter +1)
                    temp.pop()
            if len(temp) == len(nums):
                if temp not in answer:
                    answer.append(temp[:])
                return
            
            
            # permuFinder (nums, n, temp, answer, counter +1)
            
            
        permuFinder ( nums, n, temp, answer, 0)
        return answer
        