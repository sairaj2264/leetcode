class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        
        else:
            arr = [[1],[1,1]]
            numRows -=2

            while(numRows > 0):
                a = len(arr)
                elements = arr[a -1]
                new = []
                new.append(1)
                for i in range(1,len(elements)):
                    temp = elements[i-1] + elements[i]
                    new.append(temp)

                new.append(1)
                arr.append(new.copy())
                numRows -= 1
            return arr

        