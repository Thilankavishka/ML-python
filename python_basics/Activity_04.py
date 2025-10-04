x = int(input("Enter a number of times: "))

sum = 0
n = 1

while n <= x    :
    num = int(input(f"Enter a number_{n}: "))
    sum = sum + num
    n = n + 1

print("Sum is: ", sum)

""""
Enter a number of times: 10
Enter a number_1: 12
Enter a number_2: 8
Enter a number_3: 5
Enter a number_4: 2
Enter a number_5: 3
Enter a number_6: 8
Enter a number_7: 7
Enter a number_8: 5
Enter a number_9: 9
Enter a number_10: 1
Sum is:  60 """
