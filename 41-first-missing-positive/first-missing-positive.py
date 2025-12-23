class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = set(nums)
        i = 1
        while True:
            if i not in n:
                return i
            i += 1