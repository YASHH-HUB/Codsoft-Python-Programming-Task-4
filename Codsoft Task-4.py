import random

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n--- New Round ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"\nScore - You: {user_score}, Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\n--- Game Over ---")
    print(f"Final Score - You: {user_score}, Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif user_score < computer_score:
        print("The computer won the game. Better luck next time!")
    else:
        print("The game ended in a tie!")

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors!")
    print("You'll be playing against the computer.")
    play_game()