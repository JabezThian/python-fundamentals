# Question 1
with open("read_files.txt", "r") as file:
    content = file.read()
print(content)

# Question 2
with open("read_files.txt", "r") as file:
    count = 0
    for line in file:
        count += 1
print(count)

# Question 3
word = input("Enter word: ")
count2 = 0
with open("read_files.txt", "r") as file:
    for line in file:
        line = line.strip()
        if word in line:
            count2 += 1
print(count2)

