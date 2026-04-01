class TicTacToeBoard:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winner = None

    def make_move(self, row: int, col: int) -> bool:
        if self.winner or self.board[row][col] != " ":
            return False
            
        self.board[row][col] = self.current_player
        self._check_winner()
        
        if not self.winner:
            self.current_player = "O" if self.current_player == "X" else "X"
        return True

    def _check_winner(self):
        b = self.board
        lines = [
            b[0], b[1], b[2],
            [b[0][0], b[1][0], b[2][0]],
            [b[0][1], b[1][1], b[2][1]],
            [b[0][2], b[1][2], b[2][2]],
            [b[0][0], b[1][1], b[2][2]],
            [b[0][2], b[1][1], b[2][0]]
        ]
        for line in lines:
            if line[0] != " " and line[0] == line[1] == line[2]:
                self.winner = line[0]
                return