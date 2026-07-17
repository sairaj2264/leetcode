class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        i = 1
        summ = 1
        peek = 0
        n = len(ratings)
        while (i < len(ratings)):
            print(summ)

            if ratings[i] == ratings[i - 1]:
                summ += 1
                i+=1
                continue

            peek = 1
            while ( i < n and ratings[i] > ratings[i -1]):
                peek += 1
                summ += peek
                i += 1
            
            down = 1
            while (i < n and ratings[i] < ratings[i-1]):
                

                summ += down
                down += 1
                i += 1
            
            if peek < down:
                summ += down - peek
        return summ 
            
                