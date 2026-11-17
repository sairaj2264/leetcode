class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_length = 100001
        min_i = -1
        min_j = -2
        answer = []
        ref_hm = {}
        hm = {}
        for i in range(0 , len(t)):
            element = t[i]
            ref_hm[element] = ref_hm.get(element, 0) + 1
            hm[element] = 0

        i = -1
        j = 0


        def check_filled():
            for key in ref_hm:
                a = hm.get(key, 0)
                b = ref_hm.get(key, 0)
                if a >= b:
                    continue
                else:
                    return False
            return True




        while j < len(s):
            element = s[j]
            exists = hm.get(element,-1)


            if exists != -1:
                hm[element] += 1
                if i == -1:
                    i = j
                is_filled = check_filled()



                if hm[s[i]] > ref_hm[s[i]] and is_filled == True:
                    hm[s[i]] -= 1
                    i += 1
                    while i < j:
                        freq = hm.get(s[i], -1)
                        if freq == -1:
                            i += 1
                        elif freq > ref_hm[s[i]]:
                            hm[s[i]] -= 1
                            i += 1
                        elif freq <= ref_hm[s[i]]:
                            break
                        else:
                            i += 1

                    length = j - i + 1
                    if length < min_length:
                        min_length = length
                        min_i = i
                        min_j = j
                    j+=1

                elif hm[s[i]] == ref_hm[s[i]] and is_filled == True:
                    length = j - i + 1
                    if length < min_length:
                        min_length = length
                        min_i = i
                        min_j = j
                    j+=1
                else:
                    j += 1
            else:
                j += 1




        i = min_i
        temp = check_filled()
        while i <= min_j and temp == True:
            answer.append(s[i])
            i+=1

        ans = ''.join(answer)
        return ans


                        
                        

