# Question 1
score = float(input("What is your current score? "))
if score < 60:
    print("F")



if 90 <= score <= 100:
    print("A")
else:
    if 80 <= score < 90:
        print("B")
    else:
        if 70<= score < 80:
            print("C")
        else:
            if 60 <= score < 70:
                print("D")
            else:
                if 60 > score > 0:
                    print("F")
                else:
                    print("Invalid grade")

# Question 2:
year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")

# Question 3
temp = float(input("Enter a temperature: "))
if temp < 15:
    print("Cold")
elif 30 > temp >= 15:
    print("Warm")
else:
    print("Hot")

