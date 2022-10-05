import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),os.pardir))
#from .game import Grid, Player,Cell
from connect4.game import Grid, Player,Cell


class DumbIA(Player):
    """IA which play on the column of the first possible empty cell it finds."""


    def play(self, grid: Grid) -> int:
        for i in range(6):
            for j in range(7):
                cell=grid.grid[i][j]
                if cell==Cell.EMPTY:
                    print(grid)
                    return j




