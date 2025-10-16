class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictt = {}
        n = len(nums)
        for i in range(n):
            val = nums[i]
            dictt[val] = dictt.get(val,0) + 1

        duplicates = []
        for key,value in dictt.items():
            if value > 1:
                duplicates.append(key)

        for i in range(len(duplicates)):
            value = duplicates[i]
            p1 = -1
            p2 = -1
            for j in range(0,n):
                if nums[j] == value and p1 < 0:
                    p1 = j
                elif  nums[j] == value and p2 < 0:
                    p2 = j
                if p1 > -1 and p2 >-1:
                    diff = abs(p1-p2)
                    if diff <= k and p1!=p2 and nums[p1] == nums[p2]:
                        return True
                    else:
                        p1 = p2
                        p2 = -1

        return False    


        