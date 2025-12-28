@cache
def helper(digs, diff, oe):
    if digs <= 0:
        return 0
    if digs == 0 and diff == 0:
        return 1
    if digs == 1:
        return 1 if 0 <= oe * diff <= 9 else 0
    res = 0
    for i in range(10):
        res += helper(digs - 1, diff - i * oe, -oe)
    return res
class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        '''def isBalanced(num):
            s = str(num)
            if len(s) < 2:
                return False
            oSum = 0
            eSum = 0
            for i, c in enumerate(s):
                d = int(c)
                if (i + 1) % 2 == 1:
                    oSum += d
                else:
                    eSum += d
            return oSum == eSum
        count = 0
        for num in range(low, high + 1):
            if isBalanced(num):
                count += 1
        return count'''
        def helper2(n):
            if n < 100:
                return n // 11
            n = list(str(n))
            l = len(n)
            res = 0
            diff = 0
            oe = 1
            for i, d in enumerate(n):
                j = int(d)
                for k in range(j):
                    res += helper(l - i - 1, diff + k * oe, oe)
                    if i == l - 1 and diff + k * oe == 0:
                        res += 1
                diff += j * oe
                oe = -oe

            if diff == 0:
                res += 1

            return res - 1

        return helper2(high) - helper2(low - 1)