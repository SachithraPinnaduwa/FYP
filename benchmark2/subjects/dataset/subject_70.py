class SudokuEngine:
    def __init__(self, grid: list):
        self.grid = grid
        self.history = []

    def place_number(self, row: int, col: int, num: int) -> bool:
        if self.grid[row][col] != 0:
            return False
            
        if self._is_valid(row, col, num):
            self.grid[row][col] = num
            self.history.append((row, col, num))
            return True
        return False

    def undo(self) -> bool:
        if not self.history:
            return False
        row, col, num = self.history.pop()
        self.grid[row][col] = 0
        return True

    def _is_valid(self, row: int, col: int, num: int) -> bool:
        for i in range(9):
            if self.grid[row][i] == num: return False
            if self.grid[i][col] == num: return False
            
        r_start = (row // 3) * 3
        c_start = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grid[r_start + i][c_start + j] == num:
                    return False
        return True