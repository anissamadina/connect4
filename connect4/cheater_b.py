from .game import Grid, Player,Cell


class CheaterB(Player):
    """This IA cheats and modify the grid to ensure player B wins."""

    def play(self, grid: Grid) -> int:
        i = 0
        j = 0
        for cell in range(grid.lines):
            for cell2 in range(grid.columns):
                var = grid.grid[cell][cell2]
                if var == Cell.A:
                    i += 1
                elif var == Cell.B:
                    j += 1
        if i == j:
            return 5

    print(Grid)


