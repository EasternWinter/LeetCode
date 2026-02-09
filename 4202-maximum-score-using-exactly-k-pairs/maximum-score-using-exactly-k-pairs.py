class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        '''nums1.sort()
        nums2.sort()
        ans = 0
        for i in range(k):
            ans += nums1[-1-i] * nums2[-1-i]
        return ans'''
        n1, n2 = len(nums1), len(nums2)
        @cache
        def trav(i, j, k):
            if k == 0:
                return 0
            if i == n1 or j == n2 or n1 - i < k or n2 - j < k:
                return float('-inf')
            return max(
                nums1[i] * nums2[j] + trav(i+1, j+1, k-1),
                trav(i+1, j, k),
                trav(i, j+1, k)
            )
        return trav(0, 0, k)