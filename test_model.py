# pyright: reportPrivateUsage=false
import pytest
from common_types import Player, MovePlacementType, TicTacToeInfo
from model import (
    TicTacToe,
    UltimateTicTacToeModel,
)

def test_place():
    grid = TicTacToe()
    grid.place(0,0, Player.P1)
    grid.place(0,1, Player.P1)

    assert grid.grid[0][0] == Player.P1

def test_check_winner_none():
    grid = TicTacToe()
    grid.place(0,0, Player.P1)
    grid.place(0,2, Player.P1)
    assert grid._check_winner(0,0,Player.P1) == None

def test_check_winner_row():
    grid = TicTacToe()
    grid.place(0,0, Player.P1)
    grid.place(0,1, Player.P1)
    grid.place(0,2, Player.P1)
    assert grid._check_winner(0,0,Player.P1) == Player.P1
    assert grid.winner == Player.P1
    assert grid.is_locked == True

def test_check_winner_col():
    grid = TicTacToe()
    grid.place(0,0, Player.P1)
    grid.place(1,0, Player.P1)
    grid.place(2,0, Player.P1)
    assert grid._check_winner(0,0,Player.P1) == Player.P1
    assert grid.winner == Player.P1
    assert grid.is_locked == True

def test_check_winner_hor():
    grid = TicTacToe()
    grid.place(0,0, Player.P1)
    grid.place(1,1, Player.P1)
    grid.place(2,2, Player.P1)
    assert grid._check_winner(0,0,Player.P1) == Player.P1
    assert grid.winner == Player.P1
    assert grid.is_locked == True

def test_check_winner_hor1():
    grid = TicTacToe()
    grid.place(0,2, Player.P1)
    grid.place(1,1, Player.P1)
    grid.place(2,0, Player.P1)
    assert grid._check_winner(0,0,Player.P1) == Player.P1
    assert grid.winner == Player.P1
    assert grid.is_locked == True

def test_is_not_draw():
    grid = TicTacToe()
    grid.place(2,2,Player.P1)
    assert grid.is_draw == False
    assert grid.is_locked == False

def test_is_draw():
    grid = TicTacToe()
    for n in range(3):
        for j in range(3):
            grid.place(n,j,Player.P1)
    assert grid.is_draw == True
    assert grid.is_locked == True

def test_grids():
    grid = UltimateTicTacToeModel()
    return grid

#     @property
#     def winner(self) -> Player | None:
#         'Returns the winning Player if there is currently one.'
#         ...

#     @property
#     def is_draw(self) -> bool:
#         'Returns True if the board is full. Else, False.'
#         ...

#     @property
#     def is_locked(self) -> bool:
#         'Returns True if the board is locked (i.e. there is a winner or there is a draw). Else, False.'
#         ...

#     @property
#     def grid(self) -> list[list[Player | Player]]:
#         'Returns the internal grid (Make sure to prevent accidental external mutation!)'
#         ...

#     def place(self, i: int, j: int, player: Player) -> bool:
#         'Places a given players symbol on the cell (i, j)'
#         'If successful (i.e. the board has has no winner, has not drawn, and cell (i, j) is empty), it returns True. Else, False.'
#         ...

# class UltimateTicTacToeModel:
#     def __init__(self, ...) -> None:
#         ...

#     @property
#     def small_grids(self) -> list[list[TicTacToe]]:
#         ...
#         'Returns the raw list of current the current Small Grids.'

#     @property
#     def ultimate_grid(self) -> TicTacToe:
#         """
#         Returns a TicTacToe class corresponding to
#         the status of the small grids. i.e. keeps track
#         if any player has marked their symbol on a Small
#         Grid by winning on it.
#         """
#         ...


#     @property
#     def next_forced_cell(self) -> tuple[int, int] | None:
#         """
#         Returns the coordinate (bi, bj) if the next player is forced to place on an unlocked cell. Else, it returns None (in the case that such cell is locked).
#         By default, this returns None when playing with the AnywherePlacement variant
#         """
#         ...

#     @property
#     def current_player(self) -> Player:
#         "Returns the current player."
#         ...

#     @property
#     def winner(self) -> Player | None:
#         """
#         Returns the winning Player if there is currently one.
#         Hint: Must forward this call to the ultimate_grid's winner-checking logic.
#         """
#         ...

#     @property
#     def is_draw(self) -> bool:
#         """
#         Returns True if the board is full. Else, False.
#         Hint: Must forward this call to the ultimate_grid's winner-checking logic.
#         """
#         ...

#     def place_ultimate(self, bi: int, bj: int, si: int, sj: int) -> bool:
#         """
#         Validates and performs a move based on Ultimate Tic-Tac-Toe rules (as explained in the Overview section).
#         If successful, the ultimate grid must be updated and the next player's turn advances.
#         Returns True if successful. Else, False.
#         """
#         ...
