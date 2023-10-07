# Random is imported, so a secret number is chosen as per the difficulty selected.
import random

# Greets the player.
print("I'm the Number Guessing Game")

# A dictionary that defines the difficulty levels, Keys (1,2,3), while Values (10,50,100) represent Max Limit.
difficulty_level = {
    "1": "10",
    "2": "50",
    "3": "100"}

# Guesses allowed:
GUESSES_ALLOWED = 4

# While loop is inserted to prevent the program from crashing in-case the user enters a wrong digit.
while True:
    user_difficulty_choice = input('''
Choose your difficulty:
Type '1' for 'Easy, 0-10' 
Type '2' for 'Medium, 0-50' 
Type '3' for 'Hard, 0-100'
Your Choice: ''')
    if user_difficulty_choice == "1" or user_difficulty_choice == "2" or user_difficulty_choice == "3":
        break
    else:
        print('''
Choose a valid difficultly''')

# Automatically selects a secret number, as per the difficulty selected.
difficulty = difficulty_level[user_difficulty_choice]
secret_number = random.randint(0, int(difficulty))

# This tracks the number of guess.
user_guess_counter = 0

# Keeps track of the hints used, and awards score based on the amount of hints used (Lower the better).
hint = 0

# while loop's (Condition): continues until the user guesses (4) times.
while user_guess_counter < GUESSES_ALLOWED:

    # stores user_guesses.
    user_guess = input(f'''
Make a guess: ''')
    user_guess = int(user_guess)

    # each time a guess is made, the counter for user guesses & hints go up by (1).
    user_guess_counter += 1
    hint += 1

    print(f'''
You have made {user_guess_counter} of {GUESSES_ALLOWED} choices.
''')

    # Condition for Right Guess & End-Result.
    if user_guess == secret_number:
        print(f'''
You got it, Perfect!''')
        if hint == 1:
            print('Score = 100')
        elif hint == 2:
            print('Score = 75')
        elif hint == 3:
            print('Score = 50')
        elif hint == 4:
            print('Score = 25')
        else:
            print('Score = 10')
        quit()

    # Condition for Wrong Guess.
    elif user_guess != secret_number:
        accuracy = 0
        if user_guess < secret_number:
            accuracy = ((secret_number - user_guess) / secret_number * 100)
            if 100 > accuracy >= 75:
                print("Coldest!, Hint: Guess Higher")
            if 75 > accuracy >= 50:
                print("Colder!, Hint: Guess Higher")
            if 50 > accuracy >= 25:
                print("Cold!, Hint: Guess Higher")
            if 25 > accuracy >= 0:
                print("Mild!, Hint: Guess Higher")
        if user_guess > secret_number:
            accuracy = ((user_guess - secret_number) / user_guess * 100)
            if 100 > accuracy >= 75:
                print("Hottest!, Hint: Guess Lower")
            if 75 > accuracy >= 50:
                print("Hotter!, Hint: Guess Lower")
            if 50 > accuracy >= 25:
                print("Hot!, Hint: Guess Lower")
            if 25 > accuracy >= 0:
                print("Mild!, Hint: Guess Lower")
    continue

# If all guesses are wrong, the end Result.
if user_guess_counter == GUESSES_ALLOWED:
    print(f'''
You lost!
Score: 0

The Secret Number was: {secret_number}.''')
