class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        answer = [-1, -1]

        maxx = float('-inf')

        for i in range (0 , len(nums)):
            for j in range(i+1, len(nums)):
                summ = nums[i] + nums[j]
                if summ == target and nums[i] != nums[j]:
                    product = (nums[i] * nums[j])
                    if product > maxx:
                        maxx = product
                        if nums[i] < nums[j]:
                            answer = [j, i]
                        else:
                            answer = [i,j]

        return answer

        