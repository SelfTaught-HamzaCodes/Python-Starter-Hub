# Exercise Seven - (For Loops & List Methods)

letters = ["s", "o", "f", "t", "w", "a", "r", "e", "e", "x", "p", "e", "r", "t"]
# or list_of_strings (as per question).

vowels = ["a", "e", "i", "o", "u"]
# we define a list, which contains all the vowels.

vowels_count = 0
# as per the question, this counter will display the vowels in the end.

letters_vowels = []
# this list will contain all the vowels in the list of letters above.

for le in letters:
    # we call the For Loop to iterate each letter in the list of letters.

    if le in vowels:
        # we say IF L is IN VOWELS (list of vowels defined above).

        letters_vowels.append(le)
        # so we append (add) the empty list with the letter le.

        vowels_count += 1
        # if the letter is in vowels list above, increment the counter by 1

    else:
        continue
print(letters_vowels)
print(f'There are: {vowels_count} vowels.')

