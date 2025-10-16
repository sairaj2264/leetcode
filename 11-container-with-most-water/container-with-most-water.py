class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        area = 0
        p1 = 0
        p2 = n -1
        while(p1<p2):
            lenn = min(height[p1],height[p2])
            widd = p2 - p1
            temp = lenn * widd
            area = max(area,temp)
            if height[p1] > height[p2]:
                p2-=1
            else:
                p1+=1

        return area 
