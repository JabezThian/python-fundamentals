# Question 1
try:
    int("abc")
except ValueError:
    print("ValueError")

# Question 2
try:
    result = "hello" + 5
    print(result)
except TypeError:
    print("TypeError")

# Question 3
a_dict = {"name": "John", "age": 18}
try:
    print(a_dict["school"])
except KeyError:
    print("KeyError")