# Email Slicer

# We ask the user to give their email.
# STRIP is used to delete any un-wanted spaces in our strings.
email = input("What is your email: ").strip()

# Square Brackets are used to access, Start of the String (:, till but not including) @.
username = email[:email.index('@')]

# Square Brackets are used to access, (+1) means 1 character ahead of @ (:, till) the end of the string.
domain = email[email.index('@')+1:]

# Result
print(f'Your Username is ({username}) and your Domain is ({domain}).')
