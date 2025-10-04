#factorial of given number
x = int(input("Enter a number: "))


def factorial(x):
 fact = 1
 for n in range(1, x + 1):
   fact = fact * n

 return fact
   

print("Factorial is: ",factorial(x))

