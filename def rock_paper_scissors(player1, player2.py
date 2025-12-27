def rock_paper_scissors(player1, player2):
    if player1 == player2:
        return "Tie"

    wins = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper",
    }

    if wins[player1] == player2:
        return "Player 1 wins"
    else:
        return "Player 2 wins"
    if __name__ == "__main__":
    print(rock_paper_scissors("Rock", "Scissors"))  # Player 1 wins
    print(rock_paper_scissors("Paper", "Rock"))     # Player 1 wins
    print(rock_paper_scissors("Scissors", "Rock"))  # Player 2 wins
    print(rock_paper_scissors("Rock", "Rock"))      # Tie