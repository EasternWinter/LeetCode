class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''ans = []
        for i in range(len(nums)-k+1):
            maxi = nums[i]
            for j in range(i, i+k-1):
                maxi = max(maxi, nums[j])
            ans.append(maxi)
        return ans'''
        heap = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output