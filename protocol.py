# In placement.py
from typing import Protocol
from common_types import TicTacToeInfo

class MovePlacement(Protocol):
    """Protocol for a move placement strategy."""

    def get_next_forced_cell(self, last_small_move: tuple[int, int], small_grids: list[list[TicTacToeInfo]]) -> tuple[int, int] | None:
        """
        Determines the next forced cell based on the last move.
        Returns (bi, bj) or None if the move is free.
        """
        ...

    def is_valid_big_cell(self, move_bi: int, move_bj: int, forced_cell: tuple[int, int] | None) -> bool:
        """Checks if the chosen big cell (bi, bj) is valid."""
        ...

class AnywherePlacement:
    """Players can play in any unlocked big grid cell."""

    def get_next_forced_cell(self, last_small_move: tuple[int, int], small_grids: list[list[TicTacToeInfo]]) -> tuple[int, int] | None:
        # Anywhere placement never forces a cell
        return None

    def is_valid_big_cell(self, move_bi: int, move_bj: int, forced_cell: tuple[int, int] | None) -> bool:
        # Any cell is valid, as long as it's not locked (which the model will check)
        return True

class ForcedPlacement:
    """Player is forced to play in the big cell corresponding to the last small move."""

    def get_next_forced_cell(self, last_small_move: tuple[int, int], small_grids: list[list[TicTacToeInfo]]) -> tuple[int, int] | None:
        si, sj = last_small_move
        # The next move is forced to big grid (si, sj)
        target_grid = small_grids[si][sj]

        if target_grid.is_locked:
            # If the forced grid is locked, the player can go anywhere
            return None
        else:
            # Otherwise, they are forced to (si, sj)
            return (si, sj)

    def is_valid_big_cell(self, move_bi: int, move_bj: int, forced_cell: tuple[int, int] | None) -> bool:
        if forced_cell is None:
            # Free move, any cell is valid
            return True
        else:
            # Must play in the forced cell
            return (move_bi, move_bj) == forced_cell