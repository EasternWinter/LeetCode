class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        '''def noSwap(string):
            maxLen = 0
            prefix = {0: -1}
            diff = 0
            for i, ch in enumerate(string):
                if ch == '0':
                    diff -= 1
                else:
                    diff += 1
                if diff in prefix:
                    maxLen = max(maxLen, i - prefix[diff])
                else:
                    prefix[diff] = i
            return maxLen
        maxLen = noSwap(s)
        sList = list(s)
        for i in range(n):
            for j in range(i+1, n):
                sList[i], sList[j] = sList[j], sList[i]
                maxLen = max(maxLen, noSwap(sList))
                sList[i], sList[j] = sList[j], sList[i]
        return maxLen'''
        def funct(s):
            freq = Counter(s)
            dict1 = defaultdict(int)
            runningSum = 0
            maxVal = 0
            for i in range(n):
                freq[s[i]] -= 1
                if s[i] == '1':
                    runningSum += 1
                else:
                    runningSum -= 1
                if runningSum == 0:
                    maxVal = max(maxVal, i+1)
                if runningSum in dict1:
                    maxVal = max(maxVal, i - dict1[runningSum])
                if freq['0'] > 0 and runningSum - 2 == 0:
                    maxVal = max(maxVal, i + 1)
                if freq['0'] > 0 and (runningSum - 2) in dict1:
                    maxVal = max(maxVal, i - dict1[runningSum - 2])
                if freq['1'] > 0 and runningSum + 2 == 0:
                    maxVal = max(maxVal, i + 1)
                if freq['1'] > 0 and (runningSum + 2) in dict1:
                    maxVal = max(maxVal, i - dict1[runningSum + 2])
                if runningSum not in dict1:
                    dict1[runningSum] = i 
            return maxVal
        return max(funct(s), funct(s[::-1]))