# Question 1
a_tuple = (1, 2, 3, 4, 5)
print(a_tuple[2])

# Question 2
list_tuple = list(a_tuple)
list_tuple[0] = 100
a_tuple = tuple(list_tuple)
print(a_tuple)

# Question 3
a, b, c, d, e = a_tuple
print(a, b, c, d, e)