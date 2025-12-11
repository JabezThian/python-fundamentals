# Question 1
add = lambda num1, num2: num1 + num2
print(add(3, 5))

# Question 2
length = lambda s: len(s)
print(length("hello"))

# Question 3
a_list = [(1, 3), (3, 9), (4, 8), (2, 1)]
sorted_list = sorted(a_list, key=lambda element: element[1])
print(sorted_list)
