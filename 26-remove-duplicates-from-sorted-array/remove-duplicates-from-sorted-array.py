class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        a = []
        nums.insert(n,-101)
        print(nums)
        index = 0
        for i in range(0,n):
            if nums[i] != nums[i + 1]:
                a.append(nums[i])
                index += 1

        for i in range(index):
            nums[i] = a[i]
        return index
            
