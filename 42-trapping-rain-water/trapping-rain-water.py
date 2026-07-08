class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = 0
        rightMax = 0

        p1 = 0
        p2 = len(height) - 1
        total = 0
        while(p1<p2):
            leftMax = max(leftMax, height[p1])
            rightMax = max(rightMax, height[p2])
            if leftMax == 0:
                p1 += 1
                continue
            if rightMax == 0:
                p2 -= 1
                continue

            if leftMax <= rightMax:

                if height[p1] >= leftMax:
                    leftMax = height[p1]
                    p1+=1

                elif height[p1] < leftMax:
                    temp = leftMax - height[p1]
                    total += temp
                    p1+=1
            
                        # if leftMax <= rightMax:
            else:

                if height[p2] >= rightMax:
                    rightMax = height[p2]
                    p2-=1

                elif height[p2] < rightMax:
                    temp = rightMax - height[p2]
                    total += temp
                    p2-=1
        return total