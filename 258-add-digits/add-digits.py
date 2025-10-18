class Solution:
    def addDigits(self, num: int) -> int:

        while(num>9):
            sum = 0
            a = num
            while(a>0):
                sum = sum + int(a%10)
                a = a/10
            num = sum
        return num
        