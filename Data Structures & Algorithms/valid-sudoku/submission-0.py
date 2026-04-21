class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = set()
        columnset = set()
        boxset = set()
        n = len(board)

        for row in board:
            for digit in row:
                if digit.isdigit():
                    if digit in rowset:
                        return False
                    rowset.add(digit)
            rowset = set()
        
        for c in range(n):
            for k in range(n): # used for digits
                if board[k][c].isdigit():
                    digit = board[k][c]
                    if digit in columnset:
                        return False
                    columnset.add(digit)
            columnset = set()
        

        for box in range(9):
            for i in range(3):
                r = (box//3) * 3 + i
                for j in range(3):
                    c = (box % 3)*3 + j
                    if board[r][c].isdigit():
                        digit = board[r][c]
                        if digit in boxset:
                            return False
                        boxset.add(digit)
            boxset = set()
    
        return True
