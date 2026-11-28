class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words = sorted(words,key = len)
        # print(words)
        def compare(s1, s2):
            i = 0
            j = 0

            chance = 0
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    i+=1
                    j+=1
                else:
                    if chance == 0:
                        chance += 1
                        i += 1
                    else:
                        break
            if i >= len(s1) and j >= len(s2):
                return True
            
            if j >= len(s2):
                if chance == 0:
                    if i + 1 >= len(s1):
                        return True
            
                
            return False



        arr = [1] * len(words)

        answer = 1
        for i in range(1 , len(words)):
            for j in range(0 ,i):
                if len(words[j]) == (len(words[i]) - 1):
                    if compare(words[i], words[j]) == True:
                        arr[i] = max(arr[i], (arr[j] + 1))
                        answer = max(answer, arr[i])

        # print(arr)
        return answer



        