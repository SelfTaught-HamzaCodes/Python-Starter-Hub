# IF STATEMENTS (Exercise Five)

# As per the instructions,

# We take INPUT for Name & store it in a variable.
# We use STRING METHODS to make our name appear in Title() form.
# Example: miRa -> Mira.

# We take INPUT for Marks & store it in a variable.

# Grade is initialised,
# In our case we only have a single loop and this isn't necessary.
# But with multiple loops (or Nested loops) it's a must to initialise them first.

# Percentage is calculated using,
# Marks entered earlier / total marks (in our case 10)
# then multiplied by 100.

student_name = input("Name: ")
student_name = student_name.title()
marks = int(input("Marks (out of 10): "))
Grade = str("")
Percentage = int((marks / 10) * 100)
Remarks = str("")

# IF CONDITION is used for making conditions as per the question table.
if 10 >= marks >= 9:

    # F'Strings are used to dynamically enter data,
    # Only Grade and Remarks have to be changed.

    print(f'''
Name: {student_name}
Marks: {marks}
Grade: A*
Percentage: {Percentage}%   
Remarks: Flawless
''')

elif 9 > marks >= 8:
    print(f'''
Name: {student_name}
Marks: {marks}
Grade: A
Percentage: {Percentage}%  
Remarks: Great
''')

elif 8 > marks >= 7:
    print(f'''
Name: {student_name}
Marks: {marks}
Grade: B
Percentage: {Percentage}% 
Remarks: Good
''')

elif 7 > marks >= 6:
    print(f'''
Name: {student_name}
Marks: {marks}
Grade: C
Percentage: {Percentage}%  
Remarks: Fine
''')

elif 6 > marks >= 5:
    print(f'''
Name: {student_name}
Marks: {marks}
Grade: D
Percentage: {Percentage}% 
Remarks: Average
''')

elif 5 > marks >= 4:
    print(f'''
Name: {student_name}
Marks: {marks}
Grade: E
Percentage: {Percentage}%  
Remarks: Below Average
''')

elif 4 > marks >= 0:
    print(f'''
Name: {student_name}
Marks: {marks}
Grade: F
Percentage: {Percentage}%  
Remarks: Need Improvement
''')

# Else means Condition stated above aren't satisfied, that means the number entered is NOT between 0 and 10.

else:
    print("Type a number between 0 and 10 next time!")
