# Part 1 - Generating The Fibonacci Sequence

# Define an empty list called "fibonacci_sequence" to store the sequence.
fibonacci_sequence = []

print("This is a Fibonacci Sequence")

# Ask the user up to which number they would like the sequence to be generated.
fibonacci_sequence_limit = input("Till which number would you like the sequence to be: ")
fsl = int(fibonacci_sequence_limit)

# Initialize variables for the Fibonacci sequence.
x = 0
y = 1
z = 0

# Loop to generate the Fibonacci sequence up to the specified limit.
while z <= fsl:
    # Append the current value 'z' to the list.
    fibonacci_sequence.append(z)

    # Calculate the next Fibonacci number.
    z = x + y

    # Update variables 'x' and 'y'.
    x = y
    y = z

# Print the generated Fibonacci sequence.
print(fibonacci_sequence)

# Part 2 - Finding a number in the Fibonacci Sequence

# Initialize a counter to keep track of search attempts.
counter = 0

# Define a binary search function to search for a number in a sorted list.
def binary_search(numbers_list, number, left, right):
    global counter
    counter += 1

    if left > right:
        return -1

    mid = (left + right) // 2
    if number == numbers_list[mid]:
        return mid
    elif number < numbers_list[mid]:
        return binary_search(numbers_list, number, left, mid - 1)
    else:
        return binary_search(numbers_list, number, mid + 1, right)

# Perform a binary search to find the number 5 in the Fibonacci sequence.
print('\n'
      f'Your Number is at: {binary_search(fibonacci_sequence, 5, 0, len(fibonacci_sequence) - 1)}')
print('\n'
      f'It took: {counter} searches to look for the number.')
