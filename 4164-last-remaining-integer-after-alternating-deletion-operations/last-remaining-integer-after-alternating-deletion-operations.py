class Solution:
    def lastInteger(self, n: int) -> int:
        nums = range(1, n+1)
        
        while len(nums) > 1:
            nums = nums[::2][::-1]
        return nums[0]