class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictt = {}
        length = len(nums)

        for i in range(0,length):
            dictt[nums[i]] = dictt.get(nums[i],0)+1

        element = max(dictt, key = dictt.get)
        return element