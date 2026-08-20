class Solution:
    def getRow(self, numRows: int) -> List[int]:
        
        if numRows == 0:
            return [1]
        elif numRows == 1:
            return [1,1]
        
        else:
            arr = [[1],[1,1]]
            numRows -=1

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
            answer = len(arr) - 1

            return arr[answer]
