class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        sign = True
        divident = dividend
        if divident > 0 and divisor < 0:
            sign = False
        elif divident < 0 and divisor > 0:
            sign = False

        if abs(dividend) == (2 ** 31) and sign == True and abs(divisor) == 1:
            return 2147483647
        divisor = abs(divisor)
        divident = abs(divident)
        answer = 0
        while (divident >= divisor):        
            temp = 1
            ans = 0
            i = 0
            while (divident > ans):
                temp = temp << 1
                ans = divisor * temp
                i+=1
            temp = temp >> 1
            ans = divisor * temp
            divident -= ans
            answer += temp

        

        # answer = answer >> 1
        if sign == False:
            return (-1 * (answer))
        else:
            return answer