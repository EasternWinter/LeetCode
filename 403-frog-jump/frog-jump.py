class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stoneSet = set(stones)
        dp = {stone: set() for stone in stones}
        dp[stones[0]].add(0)
        for stone in stones:
            for k in dp[stone]:
                for jump in (k-1, k, k+1):
                    if jump > 0 and stone + jump in stoneSet:
                        dp[stone + jump].add(jump)
        return len(dp[stones[-1]]) > 0