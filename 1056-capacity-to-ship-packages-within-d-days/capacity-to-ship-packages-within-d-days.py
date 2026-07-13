class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        if days == 1:
            return sum(weights)
        def shipper( nums, days, x):
            i = 0
            temp = 0
            counter = 0

            while (i < len(nums)):
                # print(temp)
                if nums[i] > x:
                    return False

                if (temp + nums[i]) < x:
                    temp += nums[i]
                    i+=1
                
                elif (temp + nums[i] ) == x:
                    temp = 0
                    counter += 1
                    i+=1
                
                else:
                    temp = nums[i]
                    counter += 1
                    i+=1

                # print(temp , counter)
            if temp > 0:
                counter += 1
            if counter <= days:
                return True
            return False

        low = 1
        high = 50000 + 1
        answer = 0
        while (low <= high):
            mid = (low + high)//2

            temp = shipper(weights, days, mid)

            if temp == False:
                low = mid + 1

            elif temp == True:
                if shipper(weights, days, mid -1) == False:
                    answer = mid
                    break
                else:
                    high = mid - 1
        
        return answer

        
            



        