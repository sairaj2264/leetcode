class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


        ans = []
        total = 1 << (len(nums))

        for i in range (0 , total):
            temp = []

            for j in range(0 ,  len(nums)):
                if (i &(1 << j))> 0:
                    temp.append(nums[j])

            ans.append(temp.copy())

        return ans
