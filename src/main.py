# Start your CLI app here.
#
# Run it with:  python3 src/main.py
#
# The brief is in PROJECT.md.
import random
from unittest import main, result
game_stats = {
    "wins": 0,
    "losses": 0,
    "ties": 0
}

def display_menu():
    print("\nWelcome to Rock, Paper, Scissors!")
    print("\nMenu:")
    print("1. Play Round")
    print("2. View Stats")
    print("3. Exit")



def get_player_choice():
    choice = input("\nChoose a move (rock, paper, or scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Choose a move (rock, paper, or scissors): ").lower()
        
        return choice

    def get_computer_choice():
        return random.choice(["rock", "paper", "scissors"])

    def determine_winner(player, computer):
        if player == computer:
            return "tie"
        elif player == "rock" and computer == "scissors":
             return "win"
        elif player == "paper" and computer =="rock":
            return "win"
        elif player == "scissors" and computer == "paper":
            return "win"
        else:
            return "loss"

    def play_round():
        player = get_computer_choice()
        compouter = get_computer_choice()
      
    print("\nYou chose:", player)
    print("Computer chose:", computer)

    result = determine_winner(player, computer)

    if result == "win":
            print("You win!")
            game_stats["wins"] += 1

    elif result == "loss":
            print("You lose!")
            game_stats["losss"] += 1

    else: 
            print("It's a tie!")
            game_stats["ties"] += 1

    def display_stats():
        total_games = ()
        game_stats["wins"] 
        game_stats["losses"] 
        game_stats["ties"]

        if total_games == 0:
             win_rate = 0
        else: 
                win_rate = round((game_stats["wins"] / total_games) * 100)

        print("\nCurrent Statistics:")
        print("Games won:", game_stats["wins"])
        print("Games Lost:", game_stats["losses"])
        print("Games Tied:", game_stats["ties"])
        print("Total Games:", total_games)
        print("Win Rate:", str(win_rate) + "%")

    def main():
        print("Welcome to Rock, Paper, Scissors!")

    while True:
        display_menu()

        action = input("\nChoose an Action (Enter 1-3): ")

        if action == "1":
            play_round()

        elif action == "2":
            display_stats()

        elif action == "3":
            print("\nThanks for playing!")
            display_stats()
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()