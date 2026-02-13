class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(x):
            pieces = 1
            runSum = 0
            for num in nums:
                if runSum + num <= x:
                    runSum += num
                else:
                    pieces += 1
                    runSum = num
                    if pieces > k:
                        return False
            return True
        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left