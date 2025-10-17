class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freq1 = [0]*26

        freq2 = [0]*26

        for i in s1:
            element = i
            freq = ord(element) - ord('a')
            freq1[freq]+=1
        m = len(s1)
        n = len(s2)

        print(freq1)
        p1 = 0
        count = 0
        i = 0
        while(i<n):
            if count < m:
                element = s2[i]
                freq = ord(element) - ord('a')
                freq2[freq]+=1
                count+=1
                print(freq2)

            elif count == m:
                if freq1 == freq2:
                    return True
                else:
                    count-=1
                    element = s2[p1]
                    freq = ord(element) - ord('a')
                    freq2[freq]-=1
                    p1+=1
                    i-=1
            i+=1

        if freq1 == freq2:
            return True

            
        return False


            

        