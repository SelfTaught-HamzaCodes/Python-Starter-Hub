# Age Calculator
year_of_birth = int(input("What is your year of birth: "))
# takes year of birth (converts str => int).
current_year = int(input("What is the current year: "))
# takes current year (converts str => int).

age = str(current_year - year_of_birth)
# Firstly, Subtracts (Current Year) with (Year Of Birth) to calculate Age.
# Secondly, Age is then converted to str (from int) in-order for concatenation to work.

print("You are " + age + " years old.")  # display's age dynamically using concatenation.
# End of the Exercise.
