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
                    for j in range(4):
                        print(Grid)
                        grid.place(j, Cell.B)
                        print(Grid)
                        return j
# quand on utilise la commande ci dessous python -m connect4 --player-a CheaterB dans le terminale ça nous revois comme quoi B wins mais quand on essaye de faire le unitest cela ne fonctionne pas

