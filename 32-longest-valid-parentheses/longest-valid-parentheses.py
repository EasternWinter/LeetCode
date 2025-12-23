class Solution:
    '''def isValid(self, s: str):
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif not stack or stack.pop() != c:
                return False
        return not stack'''

    def longestValidParentheses(self, s: str) -> int:
        '''if len(s) <= 1:
            return 0
        ans = 0
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if self.isValid(s[i:j]) and j - i > ans:
                    ans = j-i
        return ans'''
        stack = []
        stack.append(-1)
        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i-stack[-1])
        return ans