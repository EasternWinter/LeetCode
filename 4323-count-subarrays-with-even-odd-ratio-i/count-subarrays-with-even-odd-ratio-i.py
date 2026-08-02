class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            even = 0
            odd = 0
            for j in range(i, n):
                if nums[j] % 2 == 1:
                    odd += 1
                else:
                    even += 1
                if odd > 0 and even / odd <= a / b:
                    count += 1
        return count