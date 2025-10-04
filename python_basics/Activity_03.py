DOB = int(input("Enter DOB: "))

age = 2025 - DOB
print("Your age is: ", age)

if age >= 18:
    print("You are Adult")
else:
    print("You are child")