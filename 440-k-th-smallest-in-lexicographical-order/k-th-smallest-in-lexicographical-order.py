class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def getGap(a, b):
            gap = 0
            while a <= n:
                gap += min(n + 1, b) - a
                a *= 10
                b *= 10
            return gap
        cur = 1
        i = 1
        while i < k:
            gap = getGap(cur, cur + 1)
            if i + gap <= k:
                i += gap
                cur += 1
            else:
                i += 1
                cur *= 10
        return cur