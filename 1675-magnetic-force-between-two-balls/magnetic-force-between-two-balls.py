class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:

        def place(nums,balls, distance):

            if balls == 1:
                return True
            previous = 0
            balls -= 1
            i = 1
            current = 0
            while (balls > 0 and i < len(nums) ):
                temp = nums[i] - nums[previous]
                if temp >= distance:
                    balls -= 1
                    previous = i
                    i+=1
                else:
                    i += 1
            if balls == 0:
                return True
            return False

        position.sort()

        high = 1000000001
        low = 1

        answer = -1
        while (low <= high):

            mid = (low + high)//2

            possible = place(position,m , mid)
            print(mid, possible)

            if possible == True:
                answer = mid
                low = mid + 1

            else:
                high = mid - 1

        return answer
            
                      
                
        