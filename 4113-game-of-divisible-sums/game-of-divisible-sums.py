class Solution:
    def maxDifference(self, nums: list[int]) -> int:
        n = len(nums)
        dp1 = 0
        dp2 = 0
        for i in range(n-1, -1, -1):
            s1 = nums[i]
            best = s1 - dp1 if s1 % 3 == 0 else s1 + dp1
            if i + 1 < n:
                s2 = nums[i] + nums[i + 1]
                cand2 = s2 - dp2 if s2 % 3 == 0 else s2 + dp2
                if cand2 > best:
                    best = cand2
            dp2 = dp1
            dp1 = best
        return dp1