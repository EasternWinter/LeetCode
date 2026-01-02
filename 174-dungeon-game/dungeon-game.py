class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        h = [[inf] * (n + 1) for _ in range(m + 1)]
        h[m][n - 1] = h[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                h[i][j] = max(1, min(h[i + 1][j], h[i][j + 1]) - dungeon[i][j])
        return h[0][0]