class Solution:
    def climbStairs(self, n: int) -> int:
        prevPrev, prev = 0, 1
        for _ in range(n):
            prevPrev, prev = prev, prevPrev + prev
        return prev