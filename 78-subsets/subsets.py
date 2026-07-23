class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


        ans = []
        def recurse(nums, temp, counter):
            if counter == len(nums):
                ans.append(temp.copy())
                return

            temp.append(nums[counter])
            recurse(nums, temp, counter + 1)
            temp.pop()
            recurse(nums, temp, counter + 1)


        temp = []
        recurse(nums, temp, 0)
        return ans            


        