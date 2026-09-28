class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxx = 0
        minn = 1000000
        profit = 0
        answer = 0
        for i in prices:
            current = i
            minn = min(minn, current)
            profit = current - minn
            answer = max(answer, profit)

        return answer

            