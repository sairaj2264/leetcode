class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        arr = nums
        x = target
        p1 = 0
        p2 = len(arr) - 1
        
        ceil = -1
        while(p1 <=p2):
            mid = (p1 + p2)//2
            

                
            if arr[mid] >= x:
                
                ceil = mid
                p2 = mid - 1
                
            elif arr[mid] < x:

                p1 = mid + 1
                

        p1 = 0
        p2 = len(arr) - 1
        
        floor = -1
        while(p1 <=p2):
            mid = (p1 + p2)//2
            

                
            if arr[mid] <= x:
                
                floor = mid
                p1 = mid + 1
                
            elif arr[mid] > x:

                p2 = mid - 1
                
        answer = []
        
        if ceil > -1 or floor > -1 :

            if arr[ceil] != x or arr[floor] != x:
                ceil, floor = -1 , -1
        answer.append(ceil)
        answer.append(floor)
        return answer