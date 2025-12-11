# Question 1
try:
    number1 = float(input("Enter a number: "))
    print(100 / number1)
except ZeroDivisionError:
    print("You can't divide by zero")

# Question 2
try:
    number2 = float(input("Enter a number: "))
    print(number2)
except ValueError:
    print("You need to enter a number")

# Question 3
try:
    with open("something.txt", "r") as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")