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
                    return True

        # TODO: Diagonal
        jeton = 0
        # First direction upper right
        for n in range(4):
            if line + n < 6 and column + n < 7 and self.grid[line + n][column + n] == color:
                jeton += 1
            else:
                break
            if jeton == 4:
                return True

        # Check the other diagonal, in the upper left direction
        jeton = 0
        for n in range(4):
            if line + n < 6 and column - n > -1 and self.grid[line + n][column - n] == color:
                jeton += 1
            else:
                break
            if jeton == 4:
                return True
        return False

    def tie(self) -> bool:
        """jeton = 0
        for j in range(7):
            compte = self.grid[5][j]
            if compte == Cell.A or compte == Cell.B:
                jeton += 1
            else:
                jeton = 0
            if jeton == 6:
                return True
            else:
                return False"""
        for line in range(self.lines):
            for col in range(self.columns):
                if self.grid[line][col] == Cell.EMPTY:
                    return False
                if self.win(line, col):
                    return False
        return True



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
