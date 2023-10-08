## Python 101
Tailored questions to challenge yourself and foster personal growth in your programming journey.
<br></br>
### Concepts
***
Aiming to master a specific concept, the following questions focus on:
1. **Question 1**: `print` statement and String Manipulation.
2. **Question 2**: `input` statement and String Concatenation.
3. **Question 3**: Type Casting (Coverting one data type to another).
4. **Question 4**: Formatted Strings (f-strings).
5. **Question 5**: `if` Statements.
6. **Question 6**: `while` Loops.
7. **Question 7**: `for` loops and List Methods.
8. **Question 8**: `dictionary`.
9. **Question 9**: Functions.
10. **Bonus Question**: `if` Statments.
<br></br>
### Questions:
***
1. **Write a program using the `print` function showing an old TV with your name written on it.** 

   - ***Hint**: `“|”` and `“_"` can be displayed as strings*
   
     ![image](https://github.com/SelfTaught-HamzaCodes/Python-Starter-Hub/assets/123310424/09c7116c-409e-46c0-8a16-a59e744736e6)

   - **Solution**: [**`print.py`**](https://github.com/SelfTaught-HamzaCodes/Python-Starter-Hub/blob/main/Python-101/print.py).
    ***
2. **Construct a program that <ins>asks</ins> the user basic information like their name, age and height, then <ins>stores</ins> it and <ins>displays</ins> it in a meaningful way.**
    - ***Hint**:*
      ```py
      age = input("age: ")  # Prompt user for age, and store it in a variable.
      print("I am " + age + " years old.")  # Display age in a meaningful way.

      # Output:
      # age: 9
      # I am 9 years old.
      ```
   - **Solution**: [**`input.py`**](https://github.com/SelfTaught-HamzaCodes/Python-Starter-Hub/blob/main/Python-101/input.py).
    ***
3. **Using the concepts of <ins>Concatenation</ins> & <ins>Coversions</ins> construct a program that can calculate age**.
    - ***Hint**: Input always stores information as string in a variable.*
    - **Solution**: [**`conversion.py`**](https://github.com/SelfTaught-HamzaCodes/Python-Starter-Hub/blob/main/Python-101/conversion.py).
   ***
4. **Using <ins>Formatted Strings</ins> construct the same Age Calculator as previously done in 
question three**.
    - **Solution**: [**`formatted_string.py`**](https://github.com/SelfTaught-HamzaCodes/Python-Starter-Hub/blob/main/Python-101/formatted_strings.py).
     ***
5. **Write a small program, that automatically grades a student based on the marks they obtain out of 10**.
    - Your code must display: Students Name, Marks, Grade, Percentage & Remarks.
    - Criteria as displayed in the table below:
    
        **Marks, Grade, Remarks**
      - Between 10 - 9, A*, Flawless
      - Between 9 - 8, A, Great
      - Between 8 - 7, B, Good
      - Between 7 - 6, C, Fine
      - Between 6 - 5, D, Average
      - Between 5 - 4, E, Below Average
      - Between 4 - 0, F, Need Improvement
    - Your code must display an error message if the marks entered at not within 
0 and 10.
    - **Solution**: [**`if_statements.py`**](https://github.com/SelfTaught-HamzaCodes/Python-Starter-Hub/blob/main/Python-101/if_statements.py).
    ***
6. **Write a small program that takes the user's email and password, stores them, and then simulates an imaginary login screen with a three-error limit. If that limit is exceeded, display a message indicating that the account is locked for one hour**.
     - **Solution**: [**`while.py`**](https://github.com/SelfTaught-HamzaCodes/Python-Starter-Hub/blob/main/Python-101/while.py).
    ***
7. **Write a small code that determines vowels from a list of strings**,
   
   `list_of_string = ["s", "o", "f", "t", "w", "a", "r", "e", "e", "x", "p", "e", "r", "t"]`
    - Your code must display the vowels.
    - Your code must tell how many vowels are there.
    - ***Hint***:
      - You can try this exercise with a string stored within a variable.
    - **Solution**: [**`for_loops_and_list_methods.py`**](https://github.com/SelfTaught-HamzaCodes/Python-Starter-Hub/blob/main/Python-101/for_loops_and_list_methods.py).
  ***
8. **Write a code which displays a word by just typing the initial alphabet.
This program will also display how many letters are there**.
    - ***Example***:
      ```py
      # Use Dictionaries to map alphabets to words.
      # Type an alphabet: a
      # Word: Apple.
      # This word has 5 letters.
      ```
   - **Solution**: [**`dictionary.py`**](https://github.com/SelfTaught-HamzaCodes/Python-Starter-Hub/blob/main/Python-101/dictionary.py).
     ***
9. **Convert question seven into a re-usable function**.

   Things to note and cover: 
      - Rather than using a list of alphabets, try passing a single word as an input.
      
        (Try: National Aeronautics and Space Act).
      - Do not include INPUT and OUTPUT in your function.
      - Do note that your function can only return a single data type, so in-order to display 
        the number of vowels detected try a work-around.
   - **Solution**: [**`function.py`**](https://github.com/SelfTaught-HamzaCodes/Python-Starter-Hub/blob/main/Python-101/functions.py).
***
#### Bonus: Fizz Buzz Challenge
Can you write a program that prints the numbers from 1 to 100? For multiples of 3, print 'Fizz' instead of the number. For multiples of 5, print 'Buzz' instead of the number. For numbers which are multiples of both 3 and 5, print 'FizzBuzz'.
- Examples:
  ```py
  number = input("Number: ")

  # TODO: Code

  # Output:
  # Number: 3
  # Fizz

  # Number: 5
  # Buzz

  # Number: 15
  # Fizz Buzz

  # Number: 4
  # 4
  ```
- **Solution**: [**`fizz_buzz.py`**](https://github.com/SelfTaught-HamzaCodes/Python-Starter-Hub/blob/main/Python-101/fizz_buzz.py)
***
Cheers,  
Muhammad Hamza Saeed
