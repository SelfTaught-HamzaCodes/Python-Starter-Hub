# Converting Exercise 7 into a re-usable function.

# We always define our function first & give it a meaningful name.
# We then set a parameter for word, where our input will go.
# We will then only copy the code that allows us to find the vowels in a given list / word.
def vowel_identifier(word):
    vowels = ["a", "e", "i", "o", "u"]
    letters_vowels = []
    for le in word:
        if le in vowels:
            letters_vowels.append(le)
        else:
            continue

    # We will return the vowels list that got identified, so we can print it out when we call the function.
    return letters_vowels


word = "National Aeronautics and Space Act"

# word.lower() is used as the predefined list of vowels only have lower-case vowels.
# You could also add upper-case vowels to the pre-defined list.
word.lower()

# we call the function and store its result in a variable.
vowels_identified = vowel_identifier(word)

print(vowels_identified)

print(f'There are {len(vowels_identified)} vowels.')
# we use length method and f strings to display the vowels found in a meaningful way,
# instead of the count method previously used.


