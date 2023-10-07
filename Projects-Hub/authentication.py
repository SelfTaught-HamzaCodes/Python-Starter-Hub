# Imports:
import sqlite3
import random
import re

# Global Variables:
quit_demo = False
path_to_database = ""


# Functions:

# Function to validate input (username, password, or email)
def validate(input_type):
    validate_un_pw = re.compile(r"^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$")
    validate_email = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")

    while True:
        entry = input(F"{input_type}: ")

        if input_type == "Username" or input_type == "Password":
            match_entry = validate_un_pw.match(entry)
        else:
            match_entry = validate_email.match(entry)

        if match_entry:
            cursor.execute(f'''SELECT EXISTS (SELECT 1 FROM users WHERE {input_type.upper()} = '{entry}') ''')
            exist = cursor.fetchone()[0]

            if exist == 0:
                return entry
            elif exist == 1:
                print(F"{entry} is already taken!")
                continue
        else:
            print(F"Enter a valid {input_type}!")
            continue


# Function to handle retrying the demo
def retry_demo():
    global quit_demo

    # Committing and closing the connection to the database
    connect.commit()
    connect.close()

    # Ask the user if they want to re-run the demo
    ask_retry = input("Retry Demo (Y - yes | N - no): ")

    if ask_retry.upper() == "N":
        quit_demo = True
    else:
        pass


# Function to handle the sign-in process
def sign_in():
    failed_attempts = 0

    while failed_attempts < 3:
        ask_email = input("Email: ")
        ask_password = input("Password: ")

        cursor.execute(F'''SELECT *
                       FROM users
                       WHERE email='{ask_email}' AND password='{ask_password}' ''')

        fetch = cursor.fetchone()

        if fetch:
            print(F"Welcome back {fetch[0]}!")
            retry_demo()
            break
        else:
            print("Invalid Email or Password")
            failed_attempts += 1

    if failed_attempts == 3:
        print("Too many failed attempts, account locked!")
        forget_password()


# Function to handle the sign-up process
def sign_up():
    ask_username = validate("Username")
    ask_email = validate("Email")
    ask_password = validate("Password")

    cursor.execute(F'''INSERT INTO users (username, email, password) 
                        VALUES ('{ask_username}', '{ask_email}', '{ask_password}') ''')

    print(F"Welcome to MH Solutions, {ask_username}")

    retry_demo()


# Function to handle password recovery
def forget_password():
    use_forget_password = input("Would you like to reset your password ? (Y - yes | N - no)")

    failed_attempts = 0

    if use_forget_password.upper() == "Y":
        while failed_attempts < 3:
            ask_email = input("Recovery Email: ")

            cursor.execute(F'''SELECT *
                            FROM users
                            WHERE email='{ask_email}' ''')

            if cursor.fetchone():
                code = str(random.randint(1000, 9999))
                print(F"Recovery Code: {code}")

                while True:
                    enter_code = input("Enter Recovery Code: ")

                    if enter_code == code:
                        new_password = input("Enter New Password: ")

                        cursor.execute(F'''UPDATE users
                        SET password='{new_password}'
                        WHERE email='{ask_email}' ''')

                        print("Done!")
                        retry_demo()
                        break
                    else:
                        print("Wrong Code!")
                        continue
                break
            else:
                print("Invalid Email")
                failed_attempts += 1
    else:
        retry_demo()

    if failed_attempts == 3:
        print("You seem to have forgotten the email as well, contact support@mhs.com for further details!")
        retry_demo()


# Main loop
while not quit_demo:
    # Connecting to the database
    connect = sqlite3.connect(path_to_database)
    cursor = connect.cursor()

    # Greet the user
    print("Welcome to MH Solutions! (DEMO)")

    # Ask the user if they want to Sign In or Sign Up
    print("Are you an existing user: Y - yes / N - no")
    user_choice = input(": ")

    if user_choice.upper() == "Y":
        sign_in()
    else:
        sign_up()

print("\nThank you for using MH Solutions, Demo!")
