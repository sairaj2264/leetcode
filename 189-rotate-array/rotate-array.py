class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        point = n - k

        p1 = 0
        p2 = point - 1
        while(p1<p2):
            temp = nums[p1]
            nums[p1] = nums[p2]
            nums[p2] = temp
            p1+=1
            p2-=1
        
        p1 = point
        p2 = n-1

        while(p1<p2):
            temp = nums[p1]
            nums[p1] = nums[p2]
            nums[p2] = temp
            p1+=1
            p2-=1


        p1 = 0
        p2 = n-1
        while(p1<p2):
            temp = nums[p1]
            nums[p1] = nums[p2]
            nums[p2] = temp
            p1 +=1
            p2 -=1

        return nums

        