class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_arry : list(int) = [0] * 9
        col_arry : list(int) = [0] * 9
        box_arry : list(int) = [0] * 9
        ROW_SIZE = COLUMN_SIZE = 9

        for row in range(ROW_SIZE):
            for col in range(COLUMN_SIZE):
                digit = board[row][col]
                if not digit.isdigit():
                    continue
                digit_bit = 1 << int(digit)
                box = 3*(row//3) + (col//3)
                if (row_arry[row] & digit_bit) or (col_arry[col] & digit_bit) or (box_arry[box] & digit_bit):
                    return False

                row_arry[row] |= digit_bit
                col_arry[col] |= digit_bit
                box_arry[box] |= digit_bit 
        

        return True