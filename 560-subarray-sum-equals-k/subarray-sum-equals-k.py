class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        dictt = {0:1}

        preSum = 0
        for i in nums:
            preSum = preSum+i
            diff = preSum - k

            a = dictt.get(diff,0)
            count+=a
            dictt[preSum] = dictt.get(preSum,0)+1

        return count


        