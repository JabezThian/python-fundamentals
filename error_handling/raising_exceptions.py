# Question 1
def custom_exception(number):
    if number < 0:
        raise IndexError("Index out of range")
    else:
        return number

# Question 2
def check_password(password):
    if len(password) < 6:
        raise IndexError("Password must be at least 6 characters long")
    else:
        return password

# Question 3
def list_check(listing):
    if len(listing) < 1:
        raise IndexError("List must be at least one element")
    else:
        return listing

# Main code, will hit error as intended
print(custom_exception(-1))
print(check_password(""))
print(list_check([]))