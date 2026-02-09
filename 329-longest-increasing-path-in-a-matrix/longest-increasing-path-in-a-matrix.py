class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans = 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[-1] * cols for _ in range(rows)]
        def travel(r, c, prev):
            if (r >= 0 and r < rows) and (c >= 0 and c < cols):
                cur = matrix[r][c]
                if cur > prev:
                    if dp[r][c] != -1:
                        return dp[r][c]
                    dp[r][c] = 1 + max(travel(r+1, c, cur), travel(r-1, c, cur), travel(r, c+1, cur), travel(r, c-1, cur))
                    return dp[r][c]
                else:
                    return 0
            else:
                return 0
        for r in range(rows):
            for c in range(cols):
                temp = travel(r, c, -1)
                if temp > ans:
                    ans = temp

        return ans