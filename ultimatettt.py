# In ultimatettt.py
from model import UltimateTicTacToeModel
from view import UltimateTicTacToeView
from controller import UltimateTicTacToeController
from protocol import AnywherePlacement, ForcedPlacement, MovePlacement
from common_types import MovePlacementType

def main() -> None:
    # Ask the user which game mode they want
    strategy: MovePlacement
    while True:
        mode = input(f"Choose mode ({MovePlacementType.ANYWHERE} or {MovePlacementType.FORCED}): ")
        if mode == MovePlacementType.ANYWHERE:
            strategy = AnywherePlacement()
            break
        elif mode == MovePlacementType.FORCED:
            strategy = ForcedPlacement()
            break
        else:
            print("Invalid mode. Please type 'Anywhere' or 'Forced'.")

    # Initialize MVC components
    model = UltimateTicTacToeModel(strategy=strategy)
    view = UltimateTicTacToeView()
    controller = UltimateTicTacToeController(model, view)

    # Run the game!
    controller.run_game()

if __name__ == "__main__":
    main()