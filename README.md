<h1>01_basics</h1>

**variables.py**
1. Create three variables: your name (string), your age (integer), and your height (float). Print each on a new line.
2. Create two variables a and b with any values. Swap their values without typing numbers again (use a temporary variable or tuple swap).
3. Create a variable with a number. Increase it using +=, then decrease it using -=, then multiply it using *=, then divide it using /=. Print after each step.

**data_types.py**
1. Start with a float value. Convert it to an integer using int(). Then convert it back to float. Print each result.
2. Ask the user to type something. Print what they typed and also print the data type using type().
3. Create a string with your name and your age. Use an f-string to print: "My name is ___ and I am ___ years old."

**input_output.py**
1. Ask the user for their name. Print: "Hello, ___!"
2. Ask the user for two numbers. Convert the inputs to integers or floats. Print their sum and product.
3. Ask the user for a sentence. Print the number of characters using len().

<h1>02_conditions </h1>

**if_else.py**
1. Ask the user for a number. If it's positive, print "Positive". If negative, print "Negative". If zero, print "Zero".
2. Ask for the user’s age.
   - If age < 13: print "Child"
   - If 13–19: print "Teen"
   - Else: print "Adult"
3. Ask for a number and check if it is even or odd using the modulus operator %.

**nested_conditions.py**
1. Ask for a score between 0 and 100.
   - 90–100 → "A"
   - 80–89 → "B"
   - 70–79 → "C"
   - 60–69 → "D"
   - <60 → "F"
   - Use nested if statements, not elif.
2. Ask for a year. Check if it is a leap year using the rules:
   - divisible by 4 
   - but not divisible by 100 
   - unless divisible by 400 
3. Ask for temperature.
   - < 15 → "Cold"
   - 15–30 → "Warm"
   - 30 → "Hot"

**logical_operators.py**
1. Ask the user for age and whether they have passed the driving test (yes/no).
Print "Eligible" only if age ≥ 18 and passed the test.
2. Ask for a username and password.
   - Check:
     - username == "admin"
     - password == "1234"
3. Ask for a number.
   - Print "In range" only if it is between 1 and 100 including boundaries.

<h1>03_loops </h1>

**for_loops.py**
1. Use a for loop to print numbers 1 to 20.
   - Take a word (string) from the user and print each character on a new line.
   - Use a for loop and range() to print even numbers from 2 to 50.

**while_loops.py**
1. Use a while loop to count backwards from 10 to 1.
2. Keep asking the user to enter text. Stop only when they type "stop".
3. Ask the user for a password. Keep asking until they enter "python123".

**loop_controls.py**
1. Loop from 1 to 10. Skip printing the number 5 using continue.
2. Loop from 1 to 20. Stop the loop completely when the number reaches 7 using break.
3. Loop from 1 to 20 and print only odd numbers.

**nested_loops.py**
1. Use nested loops to print a 3x3 square of * characters.
2. Create a multiplication table from 1 to 5 using nested loops.
3. Given a list of lists (e.g., [[1,2],[3,4],[5,6]]), use nested loops to print every element individually.

<h1>04_functions </h1>

**basic_functions.py**
1. Write a function say_hello() that prints "Hello!"
2. Write a function greet(name) that prints "Hello, <name>!"
3. Write a function square(num) that prints the square of the number.

**parameters_arguments.py**
1. Write a function that takes two numbers and prints their sum.
2. Write a function that accepts a list and prints how many items it has.
3. Write a function that accepts name and age, and prints:
   - "My name is ___ and I am ___ years old."

**return_values.py**
1. Write a function that returns the area of a rectangle given width and height.
2. Write a function that returns the largest of three numbers.
3. Write a function that returns a string reversed.

**lambda_functions.py**
1. Create a lambda function that adds two numbers.
2. Create a lambda that takes a string and returns its length.
3. Create a list of tuples. Use a lambda in sorted() to sort by the second element.

<h1>05_data_structures</h1>

**lists.py**
1. Create a list of five numbers. Print the first and last.
2. Add two new elements. Remove one element. Print the updated list.
3. Loop through the list and print only numbers greater than 10.

**tuples.py**
1. Create a tuple of five items. Print the middle item.
2. Convert the tuple to a list. Change one item. Convert back to tuple.
3. Unpack the tuple into five variables and print each.

**sets.py**
1. Create two sets with some overlapping items. Print the union.
2. Print the intersection of the two sets.
3. Add an element to one set, then remove an element.

**dictionaries.py**
1. Create a dictionary with keys: "name", "age", "country".
2. Add a new key "hobby" with any value.
3. Loop through the dictionary and print each key and value.

<h1>06_modules_packages </h1>

**importing_modules.py**
1. Import math. Print the square root of 49.
2. Import random. Print a random number between 1 and 100.
3. Import datetime. Print today’s date.

**using_math_module.py**
1. Ask the user for a radius and calculate circumference using math.pi.
2. Ask the user for a number and print its factorial using math.factorial().
3. Ask the user for a base and exponent. Use math.pow() to compute the result.

**custom_module_example/helper.py**
1. Write three simple functions such as:
   - add(a, b)
   - subtract(a, b)
   - greet(name)

**custom_module_example/main.py**
1. Import the functions from helper.py. 
2. Call each function and print the results. 
3. Try importing in two different ways:
    - import helper 
    - from helper import add

<h1>07_file_handling</h1>

**read_files.py**
(You need to create a text file manually first.)
1. Read the entire file and print its contents.
2. Read the file line by line and count how many lines there are.
3. Ask the user for a word and count how many times it appears in the file.

**write_files.py**
1. Create a list of names. Write each name on a new line into a file.
2. Append an extra name to the same file.
3. Ask the user for text and write it into a file.

**read_write_together.py**
1. Write the numbers 1–10 (each on a new line) into a file. Then read the file and print each line.
2. Write three sentences into a file. Then read the file and count how many words there are total.
3. Open one file, read its contents, and write them into a new file.

<h1>08_error_handling</h1>

**try_except.py**
1. Ask the user for a number and divide 100 by it. Handle division by zero.
2. Ask for a number. If the user enters text, handle the error using ValueError.
3. Try to open a file that does not exist and handle the exception.

**common_errors.py**
1. Force a ValueError and catch it with except.
2. Force a TypeError (e.g., add a string and number) and catch it.
3. Force a KeyError using a dictionary and catch it.

**raising_exceptions.py**
1. Create a function that raises a custom error if the input number is negative.
2. Create a function that checks password length. If < 6 characters, raise an exception.
3. Create a function that raises an error if a list passed in is empty.