class Solution:
    def minCut(self, s: str) -> int:
        if len(s) == 1:
            return 0
        N = len(s)
        dp = [-1] + [N] * N
        for i in range(N*2-1):
            l = i // 2
            r = l + (i & 1)
            while l >= 0 and r < N and s[l] == s[r]:
                dp[r+1] = min(dp[r+1], dp[l] + 1)
                l -= 1
                r += 1
        return dp[N]