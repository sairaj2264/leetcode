class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        a = []
        people = sorted(people)
        
        p1 = 0
        p2 = n-1

        while(p1<=p2):
            if people[p1] + people[p2] <= limit and p1 != p2:
                a.append(0)
                p1+=1
                p2-=1
            else:
                p2-=1
                a.append(0)
            
        ans = len(a)

        return ans

        