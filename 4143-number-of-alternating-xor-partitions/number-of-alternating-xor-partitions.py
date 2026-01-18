class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        '''if len(nums) == 1:
            if nums[0] != target1:
                return 0
            else:
                return 1
        count = 0
        for i in range(1, len(nums)+1):
            f = nums[:i]
            tF = 0
            for j in f:
                tF = tF ^ j
            if i != len(nums) and tF == target1:
                s = nums[i:]
                tS = 0
                for k in s:
                    tS = tS ^ k
                if tS == target2:
                    count += 1
            elif i == len(nums) and tF == target1:
                count += 1
        return count'''
        MOD = 10**9 + 7

        m1 = defaultdict(int)
        m2 = defaultdict(int)

        m1[0] = 1
        x = 0
        count1 = count2 = 0

        for num in nums:
            x ^= num

            t1 = x ^ target1
            t2 = x ^ target2

            count1 = m2.get(t2, 0) % MOD
            count2 = m1.get(t1, 0) % MOD

            m1[x] = (m1[x] + count1) % MOD
            m2[x] = (m2[x] + count2) % MOD

        return (count1 + count2) % MOD