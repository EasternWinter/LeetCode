class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        '''score = 0
        at = set()
        for i in range(len(s)):
            if s[i] == '1' and i == 0:
                score += nums[i]
                at.add(i)
            elif s[i] == '1':
                if at:
                    temp = 0
                    tempInd = 0
                    for j in range(max(at) + 1, i+1):
                        if nums[j] > temp:
                            temp = nums[j]
                            tempInd = j
                    score += temp
                    at.add(tempInd)
                else:
                    temp = 0
                    tempInd = 0
                    for j in range(i+1):
                        if nums[j] > temp:
                            temp = nums[j]
                            tempInd = j
                    score += temp
                    at.add(tempInd)
        return score'''
        heap = []
        score = 0
        for i in range(len(nums)):
            heappush(heap, -nums[i])
            if s[i] == '1':
                score += -heappop(heap)

        return score