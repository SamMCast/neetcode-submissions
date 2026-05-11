class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows : list[int] = [0] * 9
        cols : list[int] = [0] * 9
        boxes : list[int] = [0] * 9
        ROW_SIZE = COLUMN_SIZE = 9

        for row in range(ROW_SIZE):
            for col in range(COLUMN_SIZE):
                digit = board[row][col]
                if not digit.isdigit():
                    continue
                digit_bit = 1 << int(digit)
                box = 3*(row//3) + (col//3)

                is_duplicate = (
                    (rows[row] & digit_bit) or 
                    (cols[col] & digit_bit) or 
                    (boxes[box] & digit_bit)
                )

                if is_duplicate:
                    return False

                rows[row] |= digit_bit
                cols[col] |= digit_bit
                boxes[box] |= digit_bit 
        

        return True