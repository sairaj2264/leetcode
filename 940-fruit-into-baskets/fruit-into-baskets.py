class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        hm = {}

        i = 0
        answer = 0
        counter = 0
        for j in range(0 , len(fruits)):
            hm[fruits[j]] = hm.get(fruits[j], 0) + 1
            if len(hm) > 2:
                while(len(hm) > 2):
                    hm[fruits[i]] -= 1
                    counter -= 1
                    if hm[fruits[i]] <= 0:
                        hm.pop(fruits[i])
                    i += 1
            counter += 1
            answer = max(answer, counter)

        return answer
                    

