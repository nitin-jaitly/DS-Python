
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print(" -- " * 3)

    def is_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2-i] == player for i in range(3)):
                return True

        return False

    def is_draw(self):
        return all(self.board[row][col] != ' ' for row in range(3) for col in range(3))

    def make_move(self, row, col):
        if self.board[row][col] != ' ':
            print("Invalid move. Try again ")
            return False

        self.board[row][col] = self.current_player

        if self.is_winner(self.current_player):
            self.print_board()
            print(f"Player {self.current_player} Wins")
            return True

        if self.is_draw():
            self.print_board()
            print(f"Its a draw")
            return True

        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return False

    def play(self):
        while True:
            self.print_board()
            try:
                row = int(input(f"Player {self.current_player} enter row (0-2)"))
                col = int(input(f"Player {self.current_player} enter col (0-2)"))

                if self.make_move(row,col):
                    break
            except ValueError:
                print("Invalid input. Enter numbers between 0 and 2.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()



