class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        temp = list(range(1, n+1))
        def perm(iterable, n):
            pool = sorted(list(iterable))
            length = len(pool)
            result = []
            
            if n >= factorial(length) or n < 0:
                return None

            for i in range(length, 0, -1):
                permsRemaining = factorial(i - 1)
                index, n = divmod(n, permsRemaining)
                result.append(pool.pop(index))
                
            return result
        per = perm(temp, k-1)
        ans = ""
        for i in per:
            ans = ans + str(i)
        return ans