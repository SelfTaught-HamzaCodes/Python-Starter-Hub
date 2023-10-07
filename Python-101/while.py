# Exercise 6 (WHILE Loops)

print("\n Sign Up \n")
# Greet the user "Sign Up".

email_su = input("What is your email: ")
password_su = input("What is your password: ")
# SU - Sign Up
# Takes "email" & "password" and stores it.

limit = 0
# "limit" is an initiator that iterates by +1 each time a wrong email or password is entered on Sign In.

print("\n Sign In \n")
# Greet the user "Sign In".

while True:
    # while True, means this loop will repeat itself until the break is applied.

    email_si = input("What is your email: ")
    password_si = input("What is your password: ")
    # SI - Sign In.
    # Takes "email" & "password" and stores it.

    if (email_si == email_su) and (password_si == password_su):
        # this IF STATEMENT, compares "sign in credentials" with "sign up credentials".

        print("\n Sign In Successfully \n")
        # if the credentials match.

        break
        # as the credentials match, we break out.

    else:
        limit += 1
        # if credentials doesn't match, we iterate limit +1.

        print(f"\n Tries left {3 - limit}. \n")
        # this Formatted Strings counter display number of tries left.

        if limit == 3:
            # if "limit" equals to 3, the program quits by displaying an error message.

            print("\n Your account is locked for 1 hour. \n")
            break
        continue
