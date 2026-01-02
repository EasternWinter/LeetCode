class Solution:
    def countDigitOne(self, n: int) -> int:
        '''if n == 0:
            return 0
        c = 0
        def rec(n):
            nonlocal c
            if n < 10:
                if n == 1:
                    return 1
                else:
                    return 0
            if n % 10 == 1:
                c += 1
            return c + rec(n // 10)
        for i in range(n + 1):
            rec(i)
        return c'''
        ans = 0
        p10 = 1
        while p10 <= n:
            divisor = p10 * 10
            quotient = n // divisor
            remainder = n % divisor
            if quotient > 0:
                ans += quotient * p10
            if remainder >= p10:
                ans += min(remainder - p10 + 1, p10)
            p10 *= 10

        return ans