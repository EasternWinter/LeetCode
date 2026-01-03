class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        '''n = nums
        ans = 0
        for i in range(len(nums)):
            ind = n.index(min(n))
            if ind == 0:
                ans += n[0] * n[1]
            elif ind == len(n) - 1:
                ans += n[-1] * n[-2]
            else:
                ans += n[ind-1] * n[ind] * n[ind+1]
        return ans'''
        n = len(nums)
        arr = [1] + nums + [1]
        f = [[0] * (n + 2) for _ in range(n + 2)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    f[i][j] = max(f[i][j], f[i][k] + f[k][j] + arr[i] * arr[k] * arr[j])
        return f[0][-1]