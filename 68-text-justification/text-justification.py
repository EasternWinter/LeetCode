class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        row = []
        rowLen = 0
        for word in words:
            if rowLen + len(word) + len(row) > maxWidth:
                for i in range(maxWidth - rowLen):
                    row[i % (len(row)-1 or 1)] += ' '
                ans.append(''.join(row))
                row = []
                rowLen = 0
            row.append(word)
            rowLen += len(word)
        return ans + [' '.join(row).ljust(maxWidth)]