# Age Converter (with f strings)

year_of_birth = int(input("What is your year of birth: "))
# takes year of birth (converts str => int, for calculation purpose)

current_year = int(input("What is the current year: "))
# takes the current year (converts str => int, for calculation purpose)

age = current_year - year_of_birth
# subtracts (Current Year) from (Year of Birth) to calculate and store in Age.
# notice!
# how this time you don't need to convert age back to (str from int).
# This is the beauty and efficiency of F strings.

print(f'You are {age} years old.')
# display's age dynamically using F strings.
# notice!
# how ideally you can write the same thing in F stings compared to:# Concatenation, print("You are " + age + " years old.")
