class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        n = len(s)
        answer = []
        def stringReverser (count , n):
            if count == n:
                return 
            stringReverser(count + 1, n)
            answer.append(s[count])

        stringReverser(0, n)

        for i in range(0,n):
            s[i] = answer[i]
            

            