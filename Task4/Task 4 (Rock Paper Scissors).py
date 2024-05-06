import random

def get_user_choice():
while True:
user_choice = input("Choose rock, paper, or scissors: ").lower()
if user_choice in ['rock', 'paper', 'scissors']:
return user_choice
else:
print("Invalid choice. Please choose rock, paper, or scissors.")

def generate_computer_choice():
return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
if user_choice == computer_choice:
return "It's a tie!"
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
(user_choice == 'scissors' and computer_choice == 'paper') or \
(user_choice == 'paper' and computer_choice == 'rock'):
return "You win!"
else:
return "Computer wins!"

def play_game():
user_score = 0
computer_score = 0

while True:
print("\nRock, Paper, Scissors Game")
print("----------------------------")
user_choice = get_user_choice()
computer_choice = generate_computer_choice()

print(f"\nYou chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

result = determine_winner(user_choice, computer_choice)
print(result)

if 'win' in result:
user_score += 1
elif 'tie' not in result:
computer_score += 1

print(f"\nYour score: {user_score}")
print(f"Computer's score: {computer_score}")

play_again = input("Do you want to play again? (yes/no): ").lower()
if play_again != 'yes':
print("Thanks for playing!")
break

if __name__ == "__main__":
play_game()