# Question 1
age = int(input("Enter your age: "))
test_result = input("Did you pass your driving test? (y/n): ")
if age >= 18 and test_result == "y":
    print("Eligible")
else:
    print("Not eligible")

# Question 2
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")

# Question 3
number = float(input("Enter a number: "))
if 0 < number <= 100:
    print("In range")
else:
    print("Out of range")