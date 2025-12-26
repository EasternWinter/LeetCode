class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        '''for i, a in enumerate(nums):
            for j in range(1, indexDiff + 1):
                if i+j >= len(nums):
                    break
                if abs(a - nums[i+j]) <= valueDiff:
                    return True
        return False'''
        window = SortedList()
        n = len(nums)
        i = 0
        j = 0

        while j < n:
            upper = window.bisect_right(nums[j])
            if (upper < len(window) and window[upper] - nums[j] <= valueDiff) or (upper > 0 and nums[j] - window[upper - 1] <= valueDiff):
                return True

            window.add(nums[j])

            if len(window) == indexDiff + 1:
                window.remove(nums[i])
                i += 1

            j += 1

        return False