class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        #area of rectangle ending at matrix[i][]
        mem = [[0] * m for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    continue
                
                mem[i][j] = 1 if j == 0 else mem[i][j-1] + 1
                width = mem[i][j]
                #Traverse up row by row. Update minimum width and find area
                for k in range(i, -1, -1):
                    width = min(width, mem[k][j])
                    area = width * (i - k + 1)
                    ans = max(ans, area)
        return ans