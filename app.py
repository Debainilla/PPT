import random

import streamlit as st

from game import determine_winner

MOVES = ("rock", "paper", "scissors")


def init_state() -> None:
    for key in ("player_wins", "computer_wins", "ties"):
        if key not in st.session_state:
            st.session_state[key] = 0
    for key in ("last_player_move", "last_computer_move", "last_result"):
        if key not in st.session_state:
            st.session_state[key] = None


def reset_scoreboard() -> None:
    st.session_state.player_wins = 0
    st.session_state.computer_wins = 0
    st.session_state.ties = 0
    st.session_state.last_player_move = None
    st.session_state.last_computer_move = None
    st.session_state.last_result = None


init_state()

st.title("Rock, Paper, Scissors")

selected_move = None
button_cols = st.columns(3)
for col, move in zip(button_cols, MOVES):
    if col.button(move.capitalize(), use_container_width=True):
        selected_move = move

if selected_move:
    computer_move = random.choice(MOVES)
    result = determine_winner(selected_move, computer_move)

    if result == "player":
        st.session_state.player_wins += 1
    elif result == "computer":
        st.session_state.computer_wins += 1
    else:
        st.session_state.ties += 1

    st.session_state.last_player_move = selected_move
    st.session_state.last_computer_move = computer_move
    st.session_state.last_result = result

if st.session_state.last_result is not None:
    st.subheader("Last round")
    st.write(f"You played: **{st.session_state.last_player_move}**")
    st.write(f"Computer played: **{st.session_state.last_computer_move}**")
    result_labels = {
        "player": "You win!",
        "computer": "You lose!",
        "tie": "It's a tie!",
    }
    st.write(f"Result: **{result_labels[st.session_state.last_result]}**")

st.subheader("Scoreboard")
score_cols = st.columns(3)
score_cols[0].metric("Player wins", st.session_state.player_wins)
score_cols[1].metric("Computer wins", st.session_state.computer_wins)
score_cols[2].metric("Ties", st.session_state.ties)

if st.button("Reset scoreboard"):
    reset_scoreboard()
    st.rerun()
