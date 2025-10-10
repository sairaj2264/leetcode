class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dictt = defaultdict(int)

        for element in nums:
            dictt[element]+=1

            if len(dictt) > 2:
                for k,v in dictt.items():
                    dictt[k] -= 1
                popList = []
                for k,v in dictt.items():
                    if dictt[k] == 0:
                        popList.append(k)
                for k in popList:
                    dictt.pop(k)
        target = len(nums)//3
        ans = []
        for k in dictt:
            if nums.count(k)>target:
                ans.append(k)

        return ans
        