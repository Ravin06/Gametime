
import random

print('''
  /$$$$$$                                            /$$     /$$                        
 /$$__  $$                                          | $$    |__/                        
| $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$        /$$$$$$   /$$ /$$$$$$/$$$$   /$$$$$$ 
| $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$      |_  $$_/  | $$| $$_  $$_  $$ /$$__  $$
| $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$        | $$    | $$| $$ \ $$ \ $$| $$$$$$$$
| $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/        | $$ /$$| $$| $$ | $$ | $$| $$_____/
|  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$        |  $$$$/| $$| $$ | $$ | $$|  $$$$$$$
 \______/  \_______/|__/ |__/ |__/ \_______/         \___/  |__/|__/ |__/ |__/ \_______/                                                                                 
''')

#some games to play while you are bored
while True:
    print("\nWelcome to the Game Time gamer! Let's get started!")
    print("Which game would you like to play?")
    print("1. Rock, Paper, Scissors")
    print("2. Guess the Number")
    print("3. Tic Tac Toe")
    game_choice = input("Enter the number of the game you would like to play: ")

    if game_choice == "1":
        print("\nLet's play Rock, Paper, Scissors!")
        print("Enter your choice:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        user_choice = input("Enter the number of your choice: ")
        user_choice = int(user_choice)
        if user_choice < 1 or user_choice > 3:
            print("Invalid choice. Please enter a number between 1 and 3.")
        else:
            computer_choice = random.randint(1, 3)
            if computer_choice == 1:
                computer_choice = "Rock"
            elif computer_choice == 2:
                computer_choice = "Paper"
            else:
                computer_choice = "Scissors"
            print(f"The computer chose: {computer_choice}")
            if user_choice == computer_choice:
                print("It's a tie!")
            elif (user_choice == 1 and computer_choice == 3) or \
                (user_choice == 2 and computer_choice == 1) or \
                (user_choice == 3 and computer_choice == 2):
                print("You win!")
            else:
                print("You lose!")

    elif game_choice == "2":
        print("Let's play Guess the Number!")
        difficulty = int(input("Choose the difficulty level (1 - easy, 2, 3 - hard): "))
        if difficulty == 1:
            number = random.randint(1, 100)
            attempts = 10
        elif difficulty == 2:
            number = random.randint(1, 100)
            attempts = 5
        elif difficulty == 3:
            number = random.randint(1, 100)
            attempts = 3
        else:
            print("Invalid difficulty level. Please choose 1, 2, or 3.")
            number = 0
            attempts = 0

        if number != 0:
            print(f"I'm thinking of a number between 1 and 100. You have {attempts} attempts to guess it.")
            for attempt in range(attempts):
                guess = int(input("Enter your guess: "))
                if guess < number:
                    print("Too low!")
                elif guess > number:
                    print("Too high!")
                else:
                    print(f"Congratulations! You guessed the number in {attempt + 1} attempts.")
                    break

            if guess != number:
                print(f"Sorry, you ran out of attempts. The number was: {number}")

    elif game_choice == "3":
        print("Let's play Tic Tac Toe!")
        board = [" " for _ in range(9)]
        player = "X"
        game_over = False

        def print_board():
            print(f"{board[0]} | {board[1]} | {board[2]}")
            print("-" * 5)
            print(f"{board[3]} | {board[4]} | {board[5]}")
            print("-" * 5)
            print(f"{board[6]} | {board[7]} | {board[8]}")

        def check_winner():
            for i in range(3):
                if board[i] == board[i + 3] == board[i + 6] == player or \
                    board[3 * i] == board[3 * i + 1] == board[3 * i + 2] == player:
                    return True
            if board[0] == board[4] == board[8] == player or \
                board[2] == board[4] == board[6] == player:
                return True
            return False

        while not game_over:
            print_board()
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = player
                if check_winner():
                    print_board()
                    print(f"Player {player} wins!")
                    game_over = True
                elif " " not in board:
                    print_board()
                    print("It's a tie!")
                    game_over = True
                player = "O" if player == "X" else "X"
            else:
                print("Invalid move. Please try again.")
