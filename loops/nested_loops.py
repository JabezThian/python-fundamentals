# Question 1
size = 3
for j in range(1, size+1):
    for i in range(1, size+1):
        print(f"*", end="")
    print("")

# Question 2
for num in range(1, 6):
    for num2 in range(1, 6):
        print(num*num2, end=" ")
    print()

# Question 3
list_of_list = [[1,2],[3,4],[5,6]]
for item in list_of_list:
    for element in item:
        print(element, end=" ")