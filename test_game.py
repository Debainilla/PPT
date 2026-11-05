import pytest

from game import determine_winner


@pytest.mark.parametrize(
    "player_move, computer_move",
    [
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper"),
    ],
    ids=["rock-beats-scissors", "paper-beats-rock", "scissors-beats-paper"],
)
def test_player_wins(player_move, computer_move):
    assert determine_winner(player_move, computer_move) == "player"


@pytest.mark.parametrize(
    "player_move, computer_move",
    [
        ("rock", "paper"),
        ("paper", "scissors"),
        ("scissors", "rock"),
    ],
    ids=["rock-loses-to-paper", "paper-loses-to-scissors", "scissors-loses-to-rock"],
)
def test_computer_wins(player_move, computer_move):
    assert determine_winner(player_move, computer_move) == "computer"


@pytest.mark.parametrize(
    "player_move, computer_move",
    [
        ("rock", "rock"),
        ("paper", "paper"),
        ("scissors", "scissors"),
    ],
    ids=["rock-ties", "paper-ties", "scissors-tie"],
)
def test_tie(player_move, computer_move):
    assert determine_winner(player_move, computer_move) == "tie"


@pytest.mark.parametrize(
    "player_move, computer_move",
    [
        ("lizard", "rock"),
        ("rock", "lizard"),
        ("", "rock"),
        ("rock", ""),
        ("Rock", "rock"),
        ("rock", "Rock"),
    ],
    ids=[
        "invalid-player-move",
        "invalid-computer-move",
        "empty-player-move",
        "empty-computer-move",
        "wrong-casing-player-move",
        "wrong-casing-computer-move",
    ],
)
def test_invalid_moves_raise_value_error(player_move, computer_move):
    with pytest.raises(ValueError):
        determine_winner(player_move, computer_move)
