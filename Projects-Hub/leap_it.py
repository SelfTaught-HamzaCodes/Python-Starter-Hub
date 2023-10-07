# Define a function to check if a year is a leap year.
def leap_year(year):
    # Leap years have specific rules, so we need to check them in order.

    # For Century Years (e.g., 1900, 2000, 2100):
    # Only those Century Years divisible by 400 are leap years.
    if year % 400 == 0:
        return True

    # For Non-Century Years (e.g., 1902, 2004, 2106):
    # Non-Century Years must be divisible by 4 and not divisible by 100.
    elif year % 4 == 0 and year % 100 != 0:
        return True

    # If the year doesn't meet any of the leap year conditions, it's not a leap year.
    else:
        return False


# Test the function with a year (e.g., 1996) to check if it's a leap year.
print(leap_year(1996))
