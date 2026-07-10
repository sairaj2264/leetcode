class Solution:
    def search(self, nums: List[int], target: int) -> int:

        
        p1 = 0
        p2 = len(nums) - 1

        if p2 == 0:
            if target == nums[p2]:
                return p2
            return -1
        
        while(p1 <= p2):
            
            mid = (p1 + p2)//2
            midVal = nums[mid]
            print(mid)
            if target == midVal:
                return mid
            elif target > midVal:
                p1 = mid + 1
            else:
                p2 = mid -1

        return -1


        