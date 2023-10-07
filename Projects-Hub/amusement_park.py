# Import the randint function from the random module
from random import randint

# Print a welcome message to the user and ask for their name
print("Welcome to the Joy Land!")
name = input("What is your name: ")
# Capitalize the first letter of the user's name
name_title = name.title()
print(f'Hi, {name_title}!')

# Use a try-except block to handle potential errors when getting age and height input
try:
    # Ask the user for their age and height, and convert them to integers
    age = int(input("What is your age: "))
    height = int(input("What is your height: "))

    # Define minimum age and height requirements
    age_min = 18
    height_min = 4

    # Check if the user meets the age and height requirements
    if age < age_min or height < height_min:
        # Display a message and the user's age and height if they don't meet the requirements
        print('''
Sorry,
Age Limit: 18        
Height Limit: 4
        ''')
        print(f'You are {age} years old & your height is {height} ft.')
        # Exit the program
        quit()
except ValueError:
    # Handle the case where the user enters invalid input (not a number)
    print("Invalid Entry")
    # Exit the program

# Use a while loop to repeatedly ask the user for their choice of ride
while True:
    ride = input('''
    Which ride would you like to take:
    press 'R' for RollerCoaster
    or
    press 'H' for Horror House
    : ''')
    ride_lower = ride.lower()  # Convert the user's input to lowercase for case-insensitive comparison
    if ride_lower != "h" and ride_lower != "r":
        # Check if the user entered an invalid choice
        print("Please enter H or R next time!")
    elif ride_lower == "h":
        # Display a message for the Horror House ride and generate a random transaction ID
        print("The Ghosts Await You.")
        print(f'Pay $5, transaction_id: {randint(1, 100)}')
        print("Thank You")
        # Exit the program
        break
    elif ride_lower == "r":
        # Display a message for the RollerCoaster ride and generate a random transaction ID
        print("Zoom on a Coaster through the Sky!")
        print(f'Pay $10, transaction_id: {randint(1, 100)}')
        print("Thank You")
        # Exit the program
        break
