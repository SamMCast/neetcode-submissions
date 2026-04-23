class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        We will use the 1 pass solution for this approach. This solution is much faster because we take
        advantage of the cpu's l1 cache memory scheme. Not to mention we avoid redudant reads. 
        We can use three data structures an array of size 9 each and use integers to track the digits 
        via bit manipulation. This is more efficient because it reduces our memory footprint compared using
        sets. To keep track of the sub boxes you can either convert the cell coordinates into a box coordinate.
        Since each sub box is 3 by 3 to convert a cell coordinate a box coordinate simply divide the cell coordinate
        position by 3. (row_cell//3, col_cell//3). The top leftmost box will now be (0,0) and the bottom rightmost box
        will now be (2,2). To convert this into a box number, take box_row *3 and the add the box_col. So (0,0) will 
        box 0 and (2,2) will be box 8.
        """
        rows_seen: list[int] = [0 for val in range(len(board)) ]
        columns_seen: list[int] = [0 for val in range(len(board))]
        boxes_seen: list[int] = [0 for val in range(len(board))]

        #The iterating through the data in row major order is much faster because it takes advantage of spatial locality
        for row in range(len(board)):
            for col in range(len(board[row])):
                num_str = board[row][col]
                if not num_str.isdigit():
                    continue
                num = int(num_str)
                #let's check if the row has a duplicate digit
                digit_exists_in_row = (rows_seen[row] >> num) & 1
                if digit_exists_in_row:
                    return False
                digit_exists_in_column = (columns_seen[col] >> num) & 1
                if digit_exists_in_column:
                    return False
                box= 3*(row//3) + (col//3)
                digit_exists_in_box = (boxes_seen[box] >> num) & 1
                if digit_exists_in_box:
                    return False

                mark_digit = (1 << num) 
                rows_seen[row] |= mark_digit
                columns_seen[col] |= mark_digit
                boxes_seen[box] |= mark_digit
        
        return True

