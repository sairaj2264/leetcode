class Solution:
    def countCommas(self, n: int) -> int:
        temp = n - 999

        if temp <= 0:
            return 0

        return temp
        