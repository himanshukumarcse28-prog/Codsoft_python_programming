#---Rock,Paper,Scissors Game---

import random
import time

def play_game():
    print(" Hey there! Welcome to Rock, Paper, Scissors!")
    print("You will play against the computer. First to 5 points wins.")
    print("Let’s see who’s smarter... you or the machine ")
    print("-----------------------------------------------")

    user_score = 0
    computer_score = 0
    rounds = 0
    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("\nChoose rock, paper, or scissors: ").lower().strip()

        if user_choice not in choices:
            print("That’s not a valid choice. Try again!")
            continue

        # Computer plays fairly
        computer_choice = random.choice(choices)

        print("\nComputer is thinking...")
        time.sleep(1)
        print(f"Computer chose: {computer_choice}")
        time.sleep(0.5)

        # Decide the winner
        if user_choice == computer_choice:
            print("It’s a tie! That was close.")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        rounds += 1

        # Display running score
        print(f"\n Round {rounds} Scoreboard:")
        print(f"You: {user_score} | Computer: {computer_score}")

        # Check if anyone reached 5 points
        if user_score == 5 or computer_score == 5:
            print("\n============================")
            print("Final Results:")
            print(f"You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("Congratulations! You beat the computer fair and square!")
            else:
                print("The computer takes the win this time. You’ll get it next round!")
            print("============================")
            break

        # Ask if user wants to continue early
        again = input("\nPlay next round? (yes/no): ").lower().strip()
        if again != "yes":
            print("\nThanks for playing! ")
            print(f"Final Score → You: {user_score} | Computer: {computer_score}")
            break


if __name__ == "__main__":
    play_game()
