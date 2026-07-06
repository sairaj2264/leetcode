class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        temp = []
        answer = []
        n = len(nums)

        def subSetFinder(nums, n, temp, counter, answer):
            answer.append(temp[:])

            for i in range (counter, n):
                if i != counter and nums[i] == nums[i-1]:
                    continue

                temp.append(nums[i])
                subSetFinder(nums, n, temp, i + 1, answer)
                temp.pop()


        nums.sort()
        subSetFinder(nums, n, temp, 0, answer)
        return answer