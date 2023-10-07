# Exercise 8 (Dictionaries)

# We take input from the user.
# We convert the input into upper case.
alphabet = input("Type an alphabet: ")
alphabet = alphabet.upper()

# We then define a dictionary, for each alphabet.
words = {
    "A": "Apple",
    "B": "Bowl"}

# output_word stores, dictionary.get (get is used to display error in-case key is missing).
output_word = words.get(alphabet, "N/A")

# output
print(f'Word: {output_word}.')
print(f'This word has {len(output_word)} letters.')
