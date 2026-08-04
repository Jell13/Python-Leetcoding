from collections import defaultdict

def isValidSudoku(board):
    rows = defaultdict(set())
    cols = defaultdict(set())
    boxes = defaultdict(set())

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue
            box_key = (r // 3, c // 3)
            if val in rows[r] or val in cols[c] or val in boxes[box_key]:
                return False

    return True
            