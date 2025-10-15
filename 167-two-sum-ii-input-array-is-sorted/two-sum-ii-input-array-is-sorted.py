class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers)-1

        while(p1<p2):
            summ = numbers[p1] + numbers[p2]
            if summ == target:
                ans = [p1+1,p2+1]
                return ans
            elif summ > target:
                p2 -=1
            else:
                p1+=1

        
        