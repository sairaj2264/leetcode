class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left = 0
        right = n - 1
        answer = []
        while(left <= right):
            e1 = nums[left]
            e2 = nums[right]

            if e1<0:
                e1 *= -1

            if e2 <0:
                e2 *- -1

            if e1 >= e2:
                temp = e1 * e1
                answer.append(temp)
                left += 1
            else:
                temp = e2 * e2
                answer.append(temp)
                right -= 1

        answer = answer [::-1]
        return answer