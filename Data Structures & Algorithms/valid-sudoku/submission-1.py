class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen_in_row = set()
            for num in row:
                if num.isdigit() and num in seen_in_row:
                    return False
                seen_in_row.add(num)
        
        for col in range(len(board)):
            seen_in_col = set()
            for row in range(len(board)):
                num = board[row][col]
                if num.isdigit() and num in seen_in_col:
                    return False
                seen_in_col.add(num)

        for box in range(9):
            seen_in_box = set()
            for i in range(3):
                row = (box//3) *3 + i
                for j in range(3):
                    col = (box %3)*3 + j
                    num = board[row][col]
                    if num.isdigit() and num in seen_in_box:
                        return False
                    seen_in_box.add(num)

        return True
