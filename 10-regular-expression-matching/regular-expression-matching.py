class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            # Verify if s[i] corresponds to p[j]
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            if j + 1 < len(p) and p[j+1] == '*':
                #2 options :
                # 1) ignore "char*" -> advance 2 places
                # 2) if one character matches -> advance one place
                memo[(i, j)] = (dp(i, j+2) or
                                (first_match and dp(i+1, j)))
                return memo[(i, j)]
            else:
                #Normal match: advance both pointers in the two strings
                memo[(i, j)] = first_match and dp(i+1, j+1)
                return memo[(i, j)]

        return dp(0, 0)