class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p1 = 0

        k = k%n
        break_point = n - k
        p2 = break_point -1
        
        while(p1<p2):
            nums[p1],nums[p2] = nums[p2],nums[p1]
            p1+=1
            p2-=1
        
        p1 = break_point
        p2 = n-1

        while(p1<p2):
            nums[p1],nums[p2] = nums[p2],nums[p1]
            p1+=1
            p2-=1

        p1 = 0
        p2 = n-1
        while(p1<p2):
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1+=1
            p2-=1
        
        return nums
        
