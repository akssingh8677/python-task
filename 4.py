#rock-paper-sicssors game

import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    
    user_score = 0
    computer_score = 0

    while True:
        # User Input
        user_choice = input("Choose rock, paper, or scissors (or type 'exit' to quit): ").lower()
        
        if user_choice == 'exit':
            print("Thanks for playing!")
            break
        elif user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        # Computer Selection
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # Determine Winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Score Tracking
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        # Display Scores
        print(f"Score - You: {user_score}, Computer: {computer_score}")

        # Play Again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
