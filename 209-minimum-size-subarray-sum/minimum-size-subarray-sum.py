class Solution:
    def minSubArrayLen(self, target: int, num: List[int]) -> int:
        
        nums = num
        nums.append(0)
        n = len(nums)
        i = 0
        p1 = 0
        summ = 0
        smallest = 2**31 -1 
        count = 0
        while(i<n):
            print(i)
            if summ<target:
                summ = summ+nums[i]
                count+=1
            else:
                smallest = min(smallest, count)
                summ -= nums[p1]
                p1+=1
                i-=1
                count-=1
                
            i+=1


        if smallest == 2**31 -1:
            return 0

        return smallest
            

