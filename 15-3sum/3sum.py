class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:    
        n = len(nums)
        nums.sort()
        t1 = 0
        ans = []
        sett = set()
        sett2 = set()



        while(t1< n-2):
            if nums[t1] not in sett2:
                sett2.add(nums[t1])
                p1 = t1+1
                p2 = n-1
                while(p1<p2):
                    summ = nums[p1] + nums[p2]
                    diff = summ + nums[t1]
                    if diff == 0:
                        anss = [nums[t1],nums[p1], nums[p2]]
                        if tuple(anss) not in sett:
                            sett.add(tuple(anss)) 
                            ans.append(anss)
                        p1+=1
                    elif diff > 0:
                        p2-=1
                    else:
                        p1+=1


            t1+=1
        return ans



        