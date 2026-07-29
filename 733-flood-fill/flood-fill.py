class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        from collections import deque

        q = deque()
        if image[sr][sc] == color:
            return image

        visited = [[0]* len(image[0]) for i in range (len(image))]
        default = image[sr][sc]

        def traverse(x , y, image, color, visited, default,q):
            if visited[x][y] == 1:
                return
            visited[x][y] = 1
            image[x][y] = color

            for di in range(-1, 2):

                for dj in range (-1, 2):
                    if abs(di) + abs(dj) == 1:
                        if (x + di) >= 0 and (x + di) < len(image) and (y + dj) >= 0 and (y + dj) < len(image[0]):
                            nRow = x + di
                            nCol = y + dj
                        
                            if visited[nRow][nCol] == 0 and image[nRow][nCol] == default:
                                q.append((nRow, nCol))

            while (len(q) > 0):
                element = q.pop()
                x = element[0]
                y = element[1]
                traverse(x, y, image, color, visited, default,q)

        traverse(sr, sc, image, color, visited, default, q)
        return image
                     
    