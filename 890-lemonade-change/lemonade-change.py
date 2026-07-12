class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        

        five = 0
        ten = 0

        for i in range (0 , len(bills)):

            cur = bills[i]

            if cur == 5:
                five += 1
            elif cur == 10:
                if five <=0:
                    return False
                five -= 1
                ten += 1
            else:
                if (ten == 0 and five < 3 ) or (five == 0):
                    return False
                elif ten > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -=3
                else:
                    return False
            


        return True



        # hm = {}
        # total = 0
        # answer = True

        # for i in range (len(bills)):

        #     if bills[i] == 5:
        #         hm[5] = hm.get(5, 0) + 1
        #         total += 5

        #     elif bills[i] == 10:
        #         if total >= 5:
        #             if hm[5] > 0:
        #                 hm[5] = hm.get(5,0) - 1
        #             else:
        #                 answer = False
        #                 break
        #         else:
        #             answer = False
        #             break
        #     else:
        #         if total >= 15:
        #             if hm[5] > 0:
        #                 if hm[10] > 0:
        #                     hm[5] = hm.get(5,0) - 1
        #                     hm[10] = hm.get(10 , 0) -1
        #                 elif hm[10] == 0:
        #                     if hm[5] >= 3:
        #                         hm[5] = hm.get(5, 0) -3

        #                     else:
        #                         answer = False
        #                         break
        #                 else:
        #                     answer = False
        #                     break
        #             else:
        #                 answer = False
        #                 break
        #         else:
        #             answer = False
        #             break
        # return answer
        
