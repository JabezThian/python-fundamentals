# Question 1
number = float(input("Enter number: "))
if number == 0:
    print("Zero")
elif number > 0:
    print("Positive")
else:
    print("Negative")

# Question 2
age = int(input("Enter age: "))
if age < 0:
    print("Invalid age")
elif age < 13:
    print("Child")
elif age <= 19:
    print("Teen")
else:
    print("Adult")

# Question 3
number2 = int(input("Enter an even or odd number: "))
# checking for even number
if number2 % 2 == 0:
    print(f"{number2} is Even")
else:
    print(f"{number2} is Odd")
