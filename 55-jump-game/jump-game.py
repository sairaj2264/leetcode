class Solution:
    def canJump(self, nums: List[int]) -> bool:

        arr = nums.copy()
        if nums[0] == 0 and len(nums) == 1:
            return True

        for i in range (len(arr) - 1, -1, -1):
            if arr[i] == 0:
                continue
            nextStep = i + arr[i]
            if nextStep >= len(arr) - 1:
                continue
            
            temp = nextStep
            while (i < temp):
                if arr[temp] != 0:
                    break
                else:
                    temp -= 1
            if temp == i:
                arr[i] = 0
                        
        if arr[0] == 0:
            return False
        return True 


            
        