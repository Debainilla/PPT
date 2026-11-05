VALID_MOVES = {"rock", "paper", "scissors"}

PLAYER_WINS = {
    ("rock", "scissors"),
    ("paper", "rock"),
    ("scissors", "paper"),
}


def determine_winner(player_move: str, computer_move: str) -> str:
    if player_move not in VALID_MOVES:
        raise ValueError(f"Invalid player move: {player_move!r}")
    if computer_move not in VALID_MOVES:
        raise ValueError(f"Invalid computer move: {computer_move!r}")
    if player_move == computer_move:
        return "tie"
    if (player_move, computer_move) in PLAYER_WINS:
        return "player"
    return "computer"
