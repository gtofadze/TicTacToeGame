class Player:

    def __init__(self, name):
        self.name = name  # calls self._name and assigns name


class Board:

    def __init__(self, size):
        self._size = size
        self._board = [
            [" " for j in range(size)] for i in range(size)
        ]  # Makes empty board
        self._occupied = set()  # Stores already occopied coordinates

    @property
    def board(self):
        return self._board

    def get_occ(self):
        return self._occupied

    def print_board(self):
        board = self._board
        size = self._size
        header = (f"    {i}" for i in range(size))
        str = "".join(header)
        print(str)

        i = 0
        for row in board:
            print(i, row)
            i += 1

    def place(self, sym, c1, c2):
        board = self._board
        occ = self._occupied
        occ.add((c1, c2))

        if sym in {"X", "O"}:
            board[c1][c2] = sym

        else:
            print("only X or O symbols can be selected")

    def find_winner(self):
        board = self._board
        size = self._size

        # Checking Rows
        for row in board:
            if row.count("X") == size:  # Means winner is X
                return "X"
            elif row.count("O") == size:  # Means Winner is O
                return "O"

        # Checking Columns
        for i in range(size):
            col = [row[i] for row in board]
            if col.count("X") == size:  # Means winner is X
                return "X"
            elif col.count("O") == size:  # Means Winner is O
                return "O"

        # Checking Diagonal
        diag = [board[i][i] for i in range(size)]

        if diag.count("X") == size:  # Means winner is X
            return "X"
        elif diag.count("O") == size:  # Means Winner is O
            return "O"

        return None


class TicTacToeGame:

    def __init__(self, p1, p2, size):
        self._p1 = p1
        self._p2 = p2
        self._board = Board(size)
        self._symbol_player = {"X": p1, "O": p2}
        self._winner = None
        self._is_tie = False
        self._turn = "X"

    def switch_turn(self):

        if self._turn == "X":
            self._turn = "O"

        elif self._turn == "O":
            self._turn = "X"

    def place(self):
        board = self._board
        turn_symbol = self._turn
        turn_player_name = self._symbol_player[turn_symbol].name
        occ = board.get_occ()

        print(f"{turn_player_name}'s turn to place {turn_symbol}")

        while True:

            c1 = int(input("Enter row coordinate: "))
            c2 = int(input("Enter column coordinate: "))

            if (c1, c2) not in occ:
                board.place(turn_symbol, c1, c2)
                break

            print(f"\n Given Coordinate ({c1}, {c2}) is already occupied")
            print("Enter again \n")

    def play_game(self):
        size = self._board._size
        board = self._board
        print("\n The game started \n")

        for i in range(size ** 2):

            board.print_board()
            print(" ")
            self.place()
            self._winner = board.find_winner()

            if self._winner != None:
                break

            print(" ")
            board.print_board()
            self.switch_turn()
            print(" ")
            self.place()
            self._winner = board.find_winner()

            if self._winner != None:
                break

            print(" ")
            self.switch_turn()

        if self._winner == None:
            print(" ")
            board.print_board()
            print(" ")
            print('It\'s a Tie')

        else:
            print(" ")
            board.print_board()
            print(" ")
            winner_name = self._symbol_player[self._winner].name
            print(f"The winner is {winner_name}, - {self._winner}")


print("Selecting initial Settings \n")

name1 = input("Enter name for X player: ")
player1 = Player(name1)

name2 = input("Enter name for O player: ")
player2 = Player(name2)

print(" ")

size = int(input("Select size of the board: "))
game = TicTacToeGame(player1, player2, size)

game.play_game()
