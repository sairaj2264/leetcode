class Solution:
    def check(self, nums: List[int]) -> bool:

        n = len(nums)
        flag = 0
        i = 0
        count = 1
        while (flag < 2):
            if nums[i%n] <= nums[(i+1)%n] and count < n :
                count += 1
                i+=1
            
            elif count == n:
                return True

            else:
                count = 1
                i+=1
                flag +=1

        return False


