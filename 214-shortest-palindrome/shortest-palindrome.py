class Solution:
    def shortestPalindrome(self, s: str) -> str:
        length = len(s)
        revString = s[::-1]
        for i in range(length):
            if s[:length - i] == revString[i:]:
                return revString[:i] + s
        return ""