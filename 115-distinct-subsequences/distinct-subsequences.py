class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        arr = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            arr[i][0] = 1
        for i, a in enumerate(s, 1):
            for j, b in enumerate(t, 1):
                arr[i][j] = arr[i-1][j]
                if a == b:
                    arr[i][j] += arr[i-1][j-1]

        return arr[m][n]