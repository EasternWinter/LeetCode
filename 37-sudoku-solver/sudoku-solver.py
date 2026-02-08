class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        blo = [set() for _ in range(9)]
        empty = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    ch = board[r][c]
                    row[r].add(ch)
                    col[c].add(ch)
                    blo[(r//3)*3+(c//3)].add(ch)
        def f(k):
            if k == len(empty):
                return 1
            r, c = empty[k]
            b = (r//3) * 3 + (c//3)
            for ch in '123456789':
                if ch not in row[r]and ch not in col[c]and ch not in blo[b]:
                    board[r][c]=ch
                    row[r].add(ch)
                    col[c].add(ch)
                    blo[b].add(ch)
                    if f(k+1):
                        return 1
                    board[r][c]="."
                    row[r].remove(ch)
                    col[c].remove(ch)
                    blo[b].remove(ch)
            return 0
        f(0)