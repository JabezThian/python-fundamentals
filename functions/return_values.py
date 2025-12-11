# Question 1
def area(height, width):
    return height * width

# Question 2
def largest(num1, num2, num3):
    largest_num = num1
    if num1 > num2:
        if num1 > num3:
            largest_num = num1
        else:
            largest_num = num3
    elif num2 > num3:
        largest_num = num2
    else:
        largest_num = num3
    return largest_num

def largest2(num1, num2, num3):
    return largest(num1, num2, num3)

# Question 3
def reverse_string(string):
    string = string[::-1]
    return string

# Main code
print(largest(1, 0, 10))
print(largest(5, 0, 11))
print(area(10, 2))
print(reverse_string("hello"))