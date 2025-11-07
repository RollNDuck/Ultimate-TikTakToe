# In model.py
import copy
from common_types import Player, TicTacToeInfo
# Still in model.py
from protocol import MovePlacement # Import your protocol

class TicTacToe:
    # Make sure to implement the TicTacToeInfo Protocol

    def __init__(self) -> None:
        # Use None to represent an empty cell
        self._grid: list[list[Player | None]] = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self._winner: Player | None = None
        self._move_count = 0

    @property
    def grid(self) -> list[list[Player | None]]:
        # Return a deep copy to prevent external mutation!
        return copy.deepcopy(self._grid)

    def place(self, i: int, j: int, player: Player) -> bool:
        if self.is_locked or self._grid[i][j] is not None:
            # Invalid move: game already over or cell is taken
            return False

        self._grid[i][j] = player
        self._move_count += 1
        self._check_winner(i, j, player) # Check for a win after placing
        return True

    def _check_winner(self, r: int, c: int, player: Player) -> None:
        # Check row
        if all(self._grid[r][j] == player for j in range(3)):
            self._winner = player
            return

        # Check column
        if all(self._grid[i][c] == player for i in range(3)):
            self._winner = player
            return

        # Check diagonals (only if the move was on a diagonal)
        if r == c and all(self._grid[i][i] == player for i in range(3)):
            self._winner = player
            return

        if r + c == 2 and all(self._grid[i][2-i] == player for i in range(3)):
            self._winner = player
            return

    @property
    def winner(self) -> Player | None:
        return self._winner

    @property
    def is_draw(self) -> bool:
        # It's a draw if there is no winner AND the board is full
        return self.winner is None and self._move_count == 9

    @property
    def is_locked(self) -> bool:
        # The grid is locked if there's a winner or it's a draw
        return self.winner is not None or self.is_draw is True

class UltimateTicTacToeModel:
    def __init__(self, strategy: MovePlacement) -> None:
        self._strategy = strategy
        self._current_player = Player.P1

        # Create a 3x3 grid of *new*, *independent* TicTacToe objects
        self._small_grids: list[list[TicTacToe]] = [
            [TicTacToe() for _ in range(3)] for _ in range(3)
        ]

        # This one tracks the *overall* game board
        self._ultimate_grid = TicTacToe()

        # No forced cell at the start of the game
        self._next_forced_cell: tuple[int, int] | None = None

    @property
    def current_player(self) -> Player:
        return self._current_player

    @property
    def small_grids(self) -> list[list[TicTacToe]]:
        return self._small_grids

    @property
    def ultimate_grid(self) -> TicTacToe:
        return self._ultimate_grid

    @property
    def next_forced_cell(self) -> tuple[int, int] | None:
        return self._next_forced_cell

    @property
    def winner(self) -> Player | None:
        # The overall winner is just the winner of the ultimate_grid
        return self._ultimate_grid.winner

    @property
    def is_draw(self) -> bool:
        # The overall draw is just the draw of the ultimate_grid
        return self._ultimate_grid.is_draw

    def place_ultimate(self, bi: int, bj: int, si: int, sj: int) -> bool:
        # 1. --- VALIDATE MOVE ---
        # Is the chosen BIG grid valid according to the strategy?
        if not self._strategy.is_valid_big_cell(bi, bj, self._next_forced_cell):
            return False # Invalid move

        target_small_grid = self._small_grids[bi][bj]

        # Is the chosen SMALL grid already locked?
        if target_small_grid.is_locked:
            return False # Invalid move

        # 2. --- PLACE SYMBOL ---
        # Try to place the symbol in the small grid
        success = target_small_grid.place(si, sj, self._current_player)

        if not success:
            return False # Invalid move (e.g., cell was already taken)

        # 3. --- UPDATE ULTIMATE GRID ---
        # After a successful placement, check if that move won the small grid
        if target_small_grid.winner:
            # Mark the ultimate grid with the winner
            self._ultimate_grid.place(bi, bj, target_small_grid.winner)
            # Note: We don't care if the ultimate_grid.place fails
            # because it just means that cell was already won (which shouldn't happen)

        # 4. --- UPDATE GAME STATE ---
        # Determine the next forced cell
        self._next_forced_cell = self._strategy.get_next_forced_cell(
            (si, sj),
            self._small_grids
        )

        # Switch players
        self._current_player = Player.P2 if self._current_player == Player.P1 else Player.P1

        return True