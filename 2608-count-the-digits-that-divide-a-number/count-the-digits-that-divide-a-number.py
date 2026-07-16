class Solution:
    def countDigits(self, num: int) -> int:
        
        numm = num
        counter = 0
        while ( numm > 0):
            temp = (numm%10)
            # print(numm , temp)
            
            if temp !=0 and num%temp == 0:
                counter +=1
            numm = int(numm/10)

        return counter