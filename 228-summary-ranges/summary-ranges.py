class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:

        answer = []

        def adder(a,b):
            if a == b:
                answer.append(f'{a}')
            else:
                strr = f"{a}->{b}"
                answer.append(strr)

        
        low = None
        current = None
        for i in nums:
            if low is None:
                low = i
                current = i
            else:
                if current +1 == i:
                    current = i
                else:
                    adder(low, current)
                    low = i
                    current = i
        
        if low != None or current != None:
            
            adder(low,current)
        return answer



        