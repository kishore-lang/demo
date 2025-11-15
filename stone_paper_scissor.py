import random

def get_computer_choice():
    """Randomly select a choice for the computer."""
    choices = ['stone', 'paper', 'scissor']
    return random.choice(choices)

def get_user_choice():
    """Get and validate user input."""
    while True:
        user_input = input("Enter your choice (stone/paper/scissor): ").lower().strip()
        if user_input in ['stone', 'paper', 'scissor']:
            return user_input
        else:
            print("Invalid choice! Please enter 'stone', 'paper', or 'scissor'.")

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "tie"
    
    winning_combinations = {
        'stone': 'scissor',
        'paper': 'stone',
        'scissor': 'paper'
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    """Display the game result."""
    print("\n" + "="*40)
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    
    if winner == "tie":
        print("Result: It's a TIE!")
    elif winner == "user":
        print("Result: YOU WIN! 🎉")
    else:
        print("Result: COMPUTER WINS! 🤖")
    print("="*40 + "\n")

def play_game():
    """Main game loop."""
    user_score = 0
    computer_score = 0
    
    print("\n" + "="*40)
    print("Welcome to STONE PAPER SCISSOR!")
    print("="*40 + "\n")
    
    while True:
        # Get choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        # Determine winner
        winner = determine_winner(user_choice, computer_choice)
        
        # Update scores
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        # Display result
        display_result(user_choice, computer_choice, winner)
        
        # Display current scores
        print(f"Score - You: {user_score} | Computer: {computer_score}\n")
        
        # Ask to play again
        play_again = input("Do you want to play again? (yes/no): ").lower().strip()
        if play_again not in ['yes', 'y']:
            break
    
    # Display final score
    print("\n" + "="*40)
    print("FINAL SCORE:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    if user_score > computer_score:
        print("You are the overall WINNER! 🏆")
    elif computer_score > user_score:
        print("Computer is the overall WINNER! 🤖")
    else:
        print("It's an overall TIE! 🤝")
    print("="*40)
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
