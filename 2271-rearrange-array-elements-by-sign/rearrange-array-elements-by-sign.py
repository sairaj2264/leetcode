class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        size = len(nums)
        answer = [0]*(size)

        p = 0
        n = 1

        for i in nums:
            if i > 0:
                answer[p] = i
                p+=2
            else:
                answer[n] = i
                n += 2

        return answer