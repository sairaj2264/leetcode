class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        a = []

        for i in range(0,n):
            element = nums[i]
            if element != 0:
                a.append(element)



        m = len(a)

        while(m < n):
            a.append(0)
            m+=1
        print(a)

        for i in range(0 , n):
            nums[i] = a[i]
        
        