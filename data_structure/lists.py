# Question 1
alist = [1, 2, 3, 4, 5]
print(alist[0])
print(alist[-1])

# Question 2
alist.append(11)
alist.append(13)
alist.remove(1)
print(alist)

# Question 3
for element in alist:
    if element > 10:
        print(element)