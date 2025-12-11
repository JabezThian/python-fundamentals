names = ["John", "Jason", "Joe"]
with open("write_files.txt", "w") as file:
    for i in names:
        file.write(i+ "\n")

with open("write_files.txt", "a") as file:
    file.write("Joshua")

word = input("Enter a word: ")
with open("write_files2.txt", "w") as file:
    file.write(word)
