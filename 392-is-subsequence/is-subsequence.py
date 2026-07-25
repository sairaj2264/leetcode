class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        t1 = list(s)
        t2 = list(t)

        print(t1)
        print(t2)
        counter = 0
        p1 = 0
        p2 = 0
        # print(len(t1))
        while(p1 < len(t1) and p2 < len(t2)):
            if t1[p1] == t2[p2]:
                p1 += 1
                counter +=1
            p2 += 1

        if counter == len(t1):
            return True
        return False