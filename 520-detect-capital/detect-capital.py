class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        summ_normal = 0
        summ_upper = 0
        n = len(word)

        a = False

        if n == 2:
            if word[0] == word[0].upper() and word[1] != word[1].upper():
                a = True

        if n > 2:
            if word[0] == word[0].upper() and word[1] != word[1].upper() and word[2] != word[2].upper():
                a = True


        for i in range(n):
            summ_normal += ord(word[i])
            summ_upper += ord(word[i].upper())
        
        
        val = summ_normal - summ_upper
        vall = (summ_upper + 32*n) - summ_normal

        if val == 0:
            return True

        elif vall == 32 and a == True:
            return True
        
        temp = 32 * n
        if val == temp:
            return True


        return False
        