import random

# Path to .txt file that contains words:
word_file = "Words.txt"

# Read a list of words from a file ('words.txt')
with open(word_file, 'r') as f:
    words = f.readlines()

# Choose a random word from the list and remove any leading/trailing whitespace
word = random.choice(words)
word = word.strip()

# Set the maximum number of allowed guesses
allowed_guesses = 7

# Initialize an empty list to store the guessed letters
guesses = []

# Initialize a flag 'done' to track if the game is over
done = False

# Main game loop
while not done:
    # Display the current state of the word with guessed letters and underscores
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")  # Display the letter if guessed
        else:
            print("_", end=" ")  # Display an underscore if not guessed
    print("")  # Print a newline after displaying the word

    # Prompt the player for their next guess and add it to the list of guesses
    guess = input(f'Allowed Errors Left: {allowed_guesses}, Next Guess: ')
    guesses.append(guess.lower())

    # Check if the guessed letter is not in the word; if so, decrement allowed_guesses
    if guess.lower() not in word.lower():
        allowed_guesses -= 1

        # If the player runs out of allowed guesses, exit the loop
        if allowed_guesses == 0:
            break

    # Check if all letters in the word have been guessed
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

# Game over, display the result
if done:
    print(f'You found the word, it was {word}!')
else:
    print(f'Game Over, it was {word}!')
