class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        i = 0
        j = 0
        hm = {}
        total = 0
        def checker():
            aa = hm.get('a', 0)
            bb = hm.get('b', 0)
            cc = hm.get('c', 0)
            if aa > 0 and bb > 0 and cc > 0:
                return True
            return False

        
        while j < len(s):
            element = s[j]
            hm[element] = hm.get(element, 0) + 1
            while checker() == True:
                total += 1
                total += ((len(s)-1) - j)
                element_i = s[i]
                hm[element_i] -= 1
                i+=1
            
            j += 1
        return total



        