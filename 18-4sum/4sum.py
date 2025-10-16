class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        p1 = 0
        nums = sorted(nums)
        ans = []
        ans_sett = set()
        for i in range(0,n-2):
            p1 = i
            p2 = p1+1
            for j in range(p2,n-1):
                p2 = j
                p3 = p2+1
                p4 = n-1

                while(p3<p4):
                    summ = nums[p1] + nums[p2] + nums[p3] + nums[p4]
                    if summ - target == 0:
                        temp = [nums[p1],nums[p2],nums[p3],nums[p4]] 
                        if tuple(temp) not in ans_sett:
                            ans_sett.add(tuple(temp))
                            ans.append(temp)
                        p3+=1
                    if summ < target:
                        p3 += 1

                    else:
                        p4 -= 1
        
        return ans


