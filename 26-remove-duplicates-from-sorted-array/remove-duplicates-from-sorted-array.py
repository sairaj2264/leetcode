class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        numss  = []
        n = len(nums)
        i = 0
        unique = 0
        if n == 1:
            return 1
        while(i<n-1):
            if nums[i]!=nums[i+1]:
                numss.append(nums[i])
                unique = i
            i+=1
            if i == n-1 and nums[n-1]!=nums[unique]:
                numss.append(nums[n-1])
        lenn = len(numss)
        if lenn == 0:
            numss.append(nums[0])
        lenn = len(numss)
        i = 0
        while(i<lenn):
            nums[i] = numss[i]
            i+=1

        return lenn
        