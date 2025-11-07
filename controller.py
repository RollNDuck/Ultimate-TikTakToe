# In controller.py
from model import UltimateTicTacToeModel
from view import UltimateTicTacToeView

class UltimateTicTacToeController:
    def __init__(self, model: UltimateTicTacToeModel, view: UltimateTicTacToeView) -> None:
        self._model = model
        self._view = view

    def run_game(self) -> None:
        while True:
            # 1. Display the board
            self._view.display_full_board(self._model.small_grids)
            self._view.display_ultimate_grid(self._model.ultimate_grid)

            # 2. Check for game over
            if self._model.winner:
                self._view.show_winner(self._model.winner)
                break
            if self._model.is_draw:
                self._view.show_draw()
                break

            # 3. Show whose turn it is
            self._view.show_turn(self._model.current_player)

            # 4. Handle move input
            forced_cell = self._model.next_forced_cell

            while True: # Loop until a valid move is made
                if forced_cell:
                    self._view.show_forced_cell(forced_cell)
                    bi, bj = forced_cell
                    si, sj = self._view.prompt_small_cell()
                else:
                    # Free move
                    bi, bj = self._view.prompt_big_cell()
                    si, sj = self._view.prompt_small_cell()

                # 5. Try to place the move
                success = self._model.place_ultimate(bi, bj, si, sj)

                if success:
                    break # Valid move, exit the 'while True' loop
                else:
                    print("Invalid move! Try again.")