from .game import Grid, Player,Cell


class CheaterB(Player):
    """This IA cheats and modify the grid to ensure player B wins."""

    def play(self, grid: Grid) -> int:
        """win horizontal"""
        i = 0
        j = 0
        for cell in range(grid.lines):
            for cell2 in range(grid.columns):
                var = grid.grid[cell][cell2]
                if var == Cell.A:
                    i += 1
                    for i in range(4):
                        grid.place(i,Cell.B)
                        print(grid)
                        return i
                """elif var == Cell.B:
                    j += 1"""
        if i == j:
            return i
    # quand on utilise la commande ci dessous python -m connect4 --player-a CheaterB dans le terminale ça nous revois comme quoi B wins mais quand on essaye de faire le unitest cela ne fonctionne pas

