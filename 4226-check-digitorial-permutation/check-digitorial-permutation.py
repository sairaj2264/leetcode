class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:

        arr = [1,1,2,6,24,120,720,5040, 40320, 362880, 3628800]
        
        
        summ = 0



        c = list(str(n))   
        c.sort()              
        c = int("".join(c))
        

        # print(m)
        m = n

        zeroCount = 0

        temp = 0
        while (m >= 1):

            temp = int(m%10)
            # print(temp)
            m = m/10

            if temp == 0:
                summ += 1
                zeroCount += 1
            
            else:
                summ += arr[temp]
        print(summ)

        maxx = list(str(summ))
        maxx.sort(reverse = True)
        maxx = int("".join(maxx))

        tempp = list(str(summ))
        tempp.sort()
        tempp = int("".join(tempp))
        # print(tempp)
        # print(c)

        if maxx < n:
            return False

        if (summ - zeroCount) == 1 and n > 1:
            return False
        digit = n
        if digit == summ or c == summ or tempp == c:
            return True
        
        if digit < summ and digit >= (summ - zeroCount):
            return True

                
        return False
        