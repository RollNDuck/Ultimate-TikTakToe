# In view.py
from common_types import Player, TicTacToeInfo

class UltimateTicTacToeView:
    # ... (copy all the provided methods like show_turn, show_winner, etc.) ...

    def display_full_board(self, small_grids: list[list[TicTacToeInfo]]) -> None:
        print("\n=====\n")
        print("Full Board:")
        print()

        # This is the tricky part
        for bi in range(3): # Iterate through big rows
            for si in range(3): # Iterate through small rows
                line_parts = []
                for bj in range(3): # Iterate through big columns
                    small_grid = small_grids[bi][bj].grid
                    small_row = small_grid[si]
                    # Convert [None, Player.P1, None] to ". X ."
                    row_str = " ".join(cell or '.' for cell in small_row)
                    line_parts.append(row_str)
                # Join the three small rows with a big separator
                print(" | ".join(line_parts))

            if bi < 2:
                # Print the horizontal separator
                print("---+---+---")
        print()

    def display_ultimate_grid(self, ultimate_grid: TicTacToeInfo) -> None:
        print("Ultimate Tic-Tac-Toe Grid:")
        print()
        for row in ultimate_grid.grid:
            # Convert [None, Player.P1, None] to ". X ."
            print(" ".join(cell or '.' for cell in row))
        print()

    def _prompt_coords(self, prompt: str) -> tuple[int, int]:
        while True:
            try:
                raw_input = input(prompt) # e.g., "0, 1"
                i_str, j_str = raw_input.split(',')
                i, j = int(i_str.strip()), int(j_str.strip())
                if 0 <= i <= 2 and 0 <= j <= 2:
                    return i, j
                else:
                    print("Coordinates must be between 0 and 2.")
            except ValueError:
                print("Invalid format. Please enter as: i, j")

    def prompt_big_cell(self) -> tuple[int, int]:
        """Must prompt 'Enter (bi, bj): '"""
        return self._prompt_coords("Enter (bi, bj): ")

    def prompt_small_cell(self) -> tuple[int, int]:
        """Must prompt 'Enter (si, sj): '"""
        return self._prompt_coords("Enter (si, sj): ")

    # ... (the rest of the provided methods) ...
    def show_forced_cell(self, forced: tuple[int, int]) -> None:
        print(f"Forced at {forced}.")

    def show_turn(self, player: Player) -> None:
        print(f"Player {self._parse_player(player)}'s turn:")

    def show_winner(self, player: Player) -> None:
        print(f"Player {self._parse_player(player)} wins!")

    def show_draw(self) -> None:
        print("It's a draw!")

    def _parse_player(self, raw: Player) -> int:
        return 1 if raw == Player.P1 else 2