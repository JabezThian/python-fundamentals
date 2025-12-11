# Question 1
with open("read_write_together.txt", "w") as file:
    for i in range(1, 11):
        file.write(str(i) + "\n")

# Question 2
with open("read_write_together2.txt", "w") as file:
    file.write("There is a wolf\n")
    file.write("There is a cat and a wolf\n")
    file.write("There is a cat and a wolf and a pig\n")

# Question 3
with open("read_write_together2.txt", "r") as file:
    for line in file:
        line = line.strip()
        word_count = len(line.split())
        print(word_count)