class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.validateRowCol(row):
                return False
        for col in [[row[colId] for row in board] for colId in range(9)]:
            if not self.validateRowCol(col):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = []
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        square.append(board[row][col])
                if not self.validateRowCol(square):
                    return False
        
        return True
    
    def validateRowCol(self, arr):
        setV = set()
        for element in arr:
            if element != '.' and element in setV:
                return False
            if element != '.':
                setV.add(element)
        return True
