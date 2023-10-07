# Define a function called fizz_buzz that takes an input number.
def fizz_buzz(input):
    # Check if the input number is divisible by both 3 and 5.
    if (input % 3 == 0) and (input % 5 == 0):
        # If it is, return "Fizz Buzz."
        return "Fizz Buzz"
    # Check if the input number is divisible by 3.
    if input % 3 == 0:
        # If it is, return "Fizz."
        return "Fizz"
    # Check if the input number is divisible by 5.
    if input % 5 == 0:
        # If it is, return "Buzz."
        return "Buzz"
    # If none of the above conditions are met, return the input number as is.
    return input

# Call the fizz_buzz function with an example input of 15 and print the result.
print(fizz_buzz(15))
