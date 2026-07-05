class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        n = len(sentence)
        hm = {}
        for i in range(0, n):
            hm[sentence[i]] = 1
        if len(hm)!= 26:
            return False
        for value in hm:
            if value == 0:
                return False
        return True

        