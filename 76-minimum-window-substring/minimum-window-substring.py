class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len1 = len(s)
        len2 = len(t)
        if len1 < len2:
            return ""
        cT = [0]*256
        cS = [0]*256
        for char in t:
            cT[ord(char)] += 1
        start = 0
        startInd = -1
        minLen = float('inf')
        count = 0
        for j in range(len1):
            cS[ord(s[j])] += 1
            if cT[ord(s[j])] != 0 and cS[ord(s[j])] <= cT[ord(s[j])]:
                count += 1
            if count == len2:
                while cS[ord(s[start])] > cT[ord(s[start])] or cT[ord(s[start])] == 0:
                    if cS[ord(s[start])] > cT[ord(s[start])]:
                        cS[ord(s[start])] -= 1
                    start += 1
                length = j - start + 1
                if minLen > length:
                    minLen = length
                    startInd = start

        if startInd == -1:
            return ""
        return s[startInd:startInd + minLen]