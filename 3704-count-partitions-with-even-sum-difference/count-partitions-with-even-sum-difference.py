class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        i = 1

        p1 = nums[0]
        p2 = sum(nums) - nums[0]
        count = 0
        while (i <= len(nums) -1):
            if (p1 - p2)%2 == 0:
                count += 1
            
            p1 += nums[i]
            p2 -= nums[i]
            i += 1

        return count

            



