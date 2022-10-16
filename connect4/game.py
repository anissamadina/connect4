from enum import Enum


class Cell(Enum):
    """Enumeration representing a Connect4 Cell."""

    EMPTY = "."
    A = "X"
    B = "O"


class Grid:
    """Grid of 42 Cells."""

    lines = 6
    columns = 7

    def __init__(self):
        """Initialize a "self.grid" member: a list of list of Cells."""
        self.grid = [[Cell.EMPTY] * self.columns for _ in range(self.lines)]

    def __str__(self) -> str:
        """Reprensent this Grid as an ASCII image."""
        ret = ""
        for line in range(self.lines - 1, -1, -1):
            ret += "|"
            for column in range(self.columns):
                ret += self.grid[line][column].value
            ret += "|\n"
        ret += "+" + "-" * self.columns + "+\n"
        ret += " " + "".join(str(i) for i in range(self.columns)) + "\n"
        return ret

    def place(self, column: int, cell: Cell) -> int:
        """Put one Cell into one of the 7 columns of this grid. Return the line where
        the token stops."""
        for line in range(self.lines):
            if self.grid[line][column] == Cell.EMPTY:
                self.grid[line][column] = cell
                return line
        raise ValueError(f"Column {column} is full.")

    def win(self, line: int, column: int) -> bool:
        """Check if the Cell at "line" / "column" is part of 4 Cells from the same
        player in a horizontal / vertical / diagonal line."""

        adjacent = 0
        jeton = 0
        color = self.grid[line][column]

        # Horizontal
        for cell in self.grid[line]:
            #print(cell)
            if cell == color:
                adjacent += 1
                #print(adjacent)
                if adjacent == 4:
                    return True
            else:
                adjacent = 0

        # TODO: Vertical
        for cell in range(6):
            #print(cell)
            var = self.grid[cell][column]
            if var == color:
                jeton += 1
                print(jeton)
                if jeton == 4:
                    print(self.grid)
                    print("vzrtical")
                    return True
            else:
                jeton = 0

        # TODO: Diagonal
        jeton = 0
        # First direction upper right
        for n in range(5):
            if ( line + n < 6 and column + n < 7 and self.grid[line + n][column + n] == color):
                jeton += 1
                print("jeton1 =", jeton)
            else:
                jeton = 0
                break
            if jeton == 4:
                print("diagonale")
                return True
        print("jetonnn", jeton)
        # Second direction down left, but still in the same diagonal
        for n in range(5):
            if ( line - n > -1 and column - n > -1 and self.grid[line - n][column - n] == color ):
                jeton += 1
                print("jeton2 =", jeton)
                print("n2 =", n)
                print("line-n2 =", line - n)
                print("column+n2 =", column + n)
                print("line2 =", line)
                print("column2 =", column)
            else:
                jeton = 0
                break
            if jeton == 4:
                return True
        # Check the other diagonal, in the upper left direction
        for n in range(5):
            if (line + n < 6 and column - n > -1 and self.grid[line + n][column - n] == color):
                jeton += 1
                print("jeton3 =", jeton)
                print("n3 =", n)
                print("line-n3 =", line - n)
                print("column+n3 =", column + n)
                print("line3 =", line)
                print("column3 =", column)
            else:
                jeton = 0
                break
            if jeton == 4:
                print("diagonale2")
                return True
            # Second direction down left, but still in the same diagonal
        for n in range(5):
            if (line - n > -1 and column + n < 7 and self.grid[line - n][column + n] == color):
                jeton += 1
                print("jeton4 =", jeton)
                print("n4 =", n)
                print("line-n4 =", line - n)
                print("column+n4 =", column + n)
                print("line4 =", line)
                print("column4 =", column)
            else:
                jeton = 0
                break
            if jeton == 4:
                return True
        return False


    def tie(self) -> bool:
        #on vérifie colonne par colonne de la dernière ligne si elle n'est pas vide
        i = 0
        for cell2 in range(7):
            var= self.grid[5][cell2]
            if var == Cell.A or var == Cell.B:
                i += 1
            else:
                i = 0
            if i == 6:
                return True
            elif i == 0:
                return False



class Player:
    """Abstract base class for Players in this game."""

    def play(self, grid: Grid) -> int:
        """Main method for the player: show them the current grid, and ask them on which
        column they want to play."""
        raise NotImplementedError


class Game:
    """Main class of this project."""

    def __init__(self, player_a: Player, player_b: Player):
        """Initialize a new game with 2 Players and a Grid."""
        self.player_a = player_a
        self.player_b = player_b
        self.grid = Grid()

    def main(self):
        """Let players play until one of the win or the grid is full."""
        while True:
            if self.play(self.player_a, Cell.A):
                print(self.grid)
                print("A wins !")
                break
            if self.grid.tie():
                print(self.grid)
                print("Tie.")
                break
            if self.play(self.player_b, Cell.B):
                print(self.grid)
                print("B wins !")
                break
            if self.grid.tie():
                print(self.grid)
                print("Tie.")
                break

    def play(self, player: Player, cell: Cell) -> bool:
        """Process one turn for one player.

        Ask the player  on which column they want to play, ask the grid on which line
        the token stops, and check if this was a winning move."""
        column = player.play(self.grid)
        line = self.grid.place(column, cell)
        return self.grid.win(line, column)
