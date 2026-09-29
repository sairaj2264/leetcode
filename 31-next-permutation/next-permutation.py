class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        if n <= 1:
            return


        index = -1
        flag = False


        for i in range(n-1,0,-1):
            if nums[i] > nums[i-1]:
                index = i - 1
                break

        if index == -1:
            nums.sort()
        else:
            minn = float('inf')
            for i in range(n-1, index,-1):
                if nums[i] > nums[index]:
                    nums[index], nums[i] = nums[i], nums[index]
                    break

            p1 = index + 1
            p2 = n - 1

            while(p1 < p2):
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 -= 1


        




        
